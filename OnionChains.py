import click
import os
import socket
import shutil
import logging

# Default paths
DEFAULT_PROXYCHAINS_PATH = "/etc/proxychains.conf"
DEFAULT_TORRC_PATH = "/etc/tor"

# Initialize logging settings
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s')

def get_base_proxychains_config():
    """Return the base configuration for proxychains."""
    return """
dynamic_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
"""

def get_torrc_template():
    """Return the base configuration template for torrc files."""
    return """
SocksPort {socks_port}
ControlPort {control_port}
DataDirectory /var/lib/tor_{socks_port}
"""

def check_dependencies():
    """Check if required tools are installed and are compatible."""
    tools = ["tor", "proxychains"]
    for tool in tools:
        if os.system(f"which {tool}") != 0:
            raise SystemExit(f"Error: {tool} is not installed.", 1)
    logging.debug("All dependencies are installed and compatible.")

def is_port_available(port):
    """Check if a given port is available."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        available = s.connect_ex(('localhost', port)) != 0
    logging.debug(f"Port {port} available: {available}")
    return available

def get_available_socks_ports(num_circuits):
    """Calculate available socks and control ports for the given number of circuits."""
    ports = []
    socks_port = 9050
    for _ in range(num_circuits):
        while not (is_port_available(socks_port) and is_port_available(socks_port + 1)):
            socks_port += 2
        ports.append(socks_port)
        socks_port += 2
    return ports

def backup_configuration(path):
    """Backup the existing configuration."""
    try:
        backup_path = f"{path}.backup"
        if os.path.exists(path):
            shutil.copy2(path, backup_path)
            logging.info(f"Backed up existing configuration from {path} to {backup_path}")
    except Exception as e:
        logging.error(f"Failed to backup configuration: {e}")
        raise SystemExit("Exiting due to backup failure.", 1)

def generate_torrc_files(num_circuits, torrc_path):
    """Generate torrc files."""
    socks_ports = get_available_socks_ports(num_circuits)
    for socks_port in socks_ports:
        control_port = socks_port + 1
        torrc_content = get_torrc_template().format(socks_port=socks_port, control_port=control_port)
        
        try:
            with open(f"{torrc_path}/torrc.{socks_port}", "w") as torrc_file:
                torrc_file.write(torrc_content)
                logging.debug(f"Wrote to {torrc_path}/torrc.{socks_port}")
        except Exception as e:
            logging.error(f"Failed to write torrc file: {e}")
            raise SystemExit("Exiting due to file write error.", 1)

def update_proxychains(num_circuits, proxychains_path):
    """Update proxychains.conf."""
    proxychains_content = get_base_proxychains_config()
    socks_ports = get_available_socks_ports(num_circuits)
    for socks_port in socks_ports:
        proxychains_content += f"socks5 127.0.0.1 {socks_port}\n"

    try:
        with open(proxychains_path, "w") as proxychains_file:
            proxychains_file.write(proxychains_content)
            logging.debug(f"Updated {proxychains_path}")
    except Exception as e:
        logging.error(f"Failed to update proxychains.conf: {e}")
        raise SystemExit("Exiting due to file write error.", 1)

@click.command()
@click.argument('num_circuits', type=int)
@click.option('--proxychains-path', default=DEFAULT_PROXYCHAINS_PATH, help='Path to proxychains.conf')
@click.option('--torrc-path', default=DEFAULT_TORRC_PATH, help='Path to save torrc files')
@click.option('--rotate-requests', default=1, type=int, help='Number of requests to make before rotating (default is 1).')
@click.option('--verbose', is_flag=True, help='Enable verbose logging')
def generate_proxychains(num_circuits, proxychains_path, torrc_path, rotate_requests, verbose):
    """
    Generate the proxychains.conf and torrc files based on the number of circuits.
    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    logging.debug("Starting generate_proxychains...")

    if num_circuits <= 0 or num_circuits > 10:  # Example limit
        raise SystemExit("Please specify a valid number of circuits (1-10).", 1)

    check_dependencies()
    backup_configuration(proxychains_path)
    backup_configuration(torrc_path)
    
    generate_torrc_files(num_circuits, torrc_path)
    update_proxychains(num_circuits, proxychains_path)

    logging.info(f"Generated {num_circuits} torrc files in {torrc_path} and updated {proxychains_path} with rotation every {rotate_requests} requests!")

if __name__ == "__main__":
    generate_proxychains()
