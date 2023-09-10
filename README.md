
# 🌐 OnionChains

OnionChains is a robust tool crafted to streamline the creation and rotation of Tor configuration files. Teamed up with `proxychains`, it ensures dynamic request handling, allowing each network request to be channeled through a distinct Tor circuit.

## 🌟 Features

- **🛠️ Tor Configuration Generation**: Effortlessly create a specified number of Tor configuration files.
- **🔄 Dynamic ProxyChains Configuration**: Seamless auto-configuration of proxychains for dynamic requests.
- **🔓 Circumvent Internet Filters**: Route your network traffic through diverse Tor circuits, evading filters and blockages.
- **🔐 Backup Logging**: Safety first! A backup is taken before overwriting any configuration.
- **🚪 Port Management**: The script ensures that the required ports are available, making adjustments if they're occupied.
- **🔍 Dependency Checks**: Prior to execution, the script verifies if essential tools (`tor` and `proxychains`) are present, guiding users towards installation if missing.
- **📜 Verbose Logging**: Use the `--verbose` flag for an in-depth logging experience, simplifying debugging and insights.

🚀 **Usage**

The `OnionChains` script offers a myriad of command-line arguments and options, allowing you to customize its operation. Delve into the details below:

### 📜 **Command**:
```
generate_proxychains [num_circuits] [OPTIONS]
```

### 📌 **Arguments**:

- **num_circuits**: 
  - **Description**: Dictates the number of Tor circuits to be crafted. This essentially sets how many diverse paths your traffic can journey through the Tor network.
  - **Usage**: 
    ```
    generate_proxychains 3
    ```

### 🔧 **Options**:

- **--proxychains-path**:
  - **Description**: Designates the path to `proxychains.conf`. The default pathway is `/etc/proxychains.conf`.
  - **Usage**:
    ```
    --proxychains-path="/path/to/your/proxychains.conf"
    ```

- **--torrc-path**:
  - **Description**: Pinpoints the directory to house the `torrc` files. By default, it resorts to `/etc/tor`.
  - **Usage**: 
    ```
    --torrc-path="/path/to/torrc/directory"
    ```

- **--rotate-requests**:
  - **Description**: This nifty option lets you stipulate the number of requests before shuffling to a fresh Tor circuit. The default setting is 1, implying each request dons a distinct circuit.
  - **Usage**: 
    ```
    --rotate-requests=5
    ```
    > 💡 Note: In this instance, the circuit would undergo rotation post every 5 requests.

- **--verbose**:
  - **Description**: Activate this flag for an immersive logging experience, granting insights into the script's inner workings and streamlining debugging.
  - **Usage**: 
    ```
    --verbose
    ```

### 🎯 **Examples**:

1. To harness the script with default configurations and spawn 3 circuits:
    ```
    generate_proxychains 3
    ```

2. To tweak the behavior and incorporate tailored options:
    ```
    generate_proxychains 5 --proxychains-path="/custom/path/proxychains.conf" --verbose
    ```

## 🛠️ Setup & Installation

1. **🔄 System Update**: `sudo apt update`
2. **📦 Install Dependencies**: `sudo apt install tor proxychains python3-pip -y`
3. **🐍 Install Script Requirements**: `pip3 install click`
4. **🔧 Configuration of Path Constants**: By default, paths `/etc/proxychains.conf` (for proxychains) and `/etc/tor` (for torrc files) are used. Customize using the `--proxychains-path` and `--torrc-path` flags.
5. **📜 Verbose Logging**: Enable detailed logging using the `--verbose` flag.

🚫 **Note**: This script is optimized for Ubuntu. Caution is advised on other OSs, especially if anonymity is paramount.

## ⚠️ Safety Considerations

Tread carefully! Using a vast number of chains might unintentionally expose your location due to atypical network traffic patterns, jeopardizing your anonymity. A maximum of 5 chains is recommended for optimal safety.

## 🔑 Permissions

For accessing the `torrc` file, `sudo` permissions are indispensable.

## 🎯 Use Cases

### 1. 🛡️ Enhanced Anonymity in Network Scanning

For cybersecurity mavens and penetration testers, OnionChains is a shield, providing added anonymity layers during network scans. Routing `nmap` scans via varied Tor circuits using `proxychains` camouflages their identity, diminishing detection risks.

```bash
proxychains sudo nmap -sT target_ip
```

### 2. 🌐 Web Scraping with Rotating IPs

Web scraping is a treasure trove for developers and data enthusiasts. Yet, many websites thwart frequent requests by imposing rate limits or IP bans. With OnionChains, every request travels through a unique Tor circuit, essentially donning a new IP mask for each request, bypassing such barricades.

### 3. 🌍 Circumventing Geo-restrictions

Geographical content barricades? No problem! OnionChains can assist users in accessing region-restricted content by directing their network traffic via Tor circuits from varied regions.

### 4. 🕵️ Secure and Anonymous Browsing

For those in internet-censored or surveillance-heavy regions, OnionChains is their cloak of invisibility. It routes all browser traffic through an array of Tor circuits, granting access to restricted websites while minimizing surveillance risks.

## 🌐 Accessing .onion Services with Mullvad Browser and OnionChains

Mullvad browser, combined with OnionChains, can potentially unlock `.onion` services, letting you delve into the "dark web" while enjoying Mullvad's uniform fingerprinting shield.

📝 **Note**: While OnionChains paves the way to `.onion` services via Tor circuits, it's essential to realize that the Tor Browser is specifically tailored for `.onion` services, packed with unique features and security mechanisms. If `.onion` services are your prime target, the Tor Browser remains unparalleled. However, for those seeking a fusion of `.onion` access with Mullvad's uniform fingerprinting, this duo can be a potent alternative.

## 🏆 Enhanced Anonymity with Mullvad Browser

Mullvad is not just another VPN service in the crowd. Born out of a collaboration with the Tor Project, Mullvad's browser is a testament to its commitment to user privacy. This joint effort ensures that the browser is built on a foundation of expertise and a deep understanding of online anonymity challenges.

The browser is intricately designed to offer a unique feature: a uniform fingerprint. In a world where browser fingerprinting has become a prevalent technique for websites to identify and track users, Mullvad stands as a bulwark, ensuring that every user appears the same, effectively shielding them from such tracking mechanisms.

In synergy with OnionChains, Mullvad sets a new benchmark for online anonymity:

- **🔍 Uniform Fingerprint**: Mullvad's collaboration with the Tor Project ensures that its browser offers a consistent fingerprint across all its users, making individual identification a challenge.
    
- **🔄 Rotating IPs**: OnionChains complements Mullvad's fingerprinting protection by rotating the user's IP. By channeling traffic through varied Tor circuits, it ensures that the source of a request remains an enigma.
    

This combination offers a holistic approach to privacy, addressing both browser-based and network-based tracking mechanisms.

## ❗ Issues with OnionChains and Tor Browser

Mixing OnionChains with the Tor browser can be a tricky cocktail, leading to potential issues:

1. **🔄 Double Tor Routing**: Tor browser already uses the Tor network. Adding OnionChains to the mix means double-routing through Tor, which can be a drag on browsing speed.
2. **⏱️ Increased Latency**: The duo can amplify latency due to added network hops.
3. **🔍 Potential Overkill**: Both aim for anonymity. Using them simultaneously might be redundant for most scenarios, potentially drawing unwanted attention to your traffic.

Users should weigh the pros and cons, ensuring clarity on potential risks and benefits. Thorough setup testing is paramount to prevent information leaks.

## 💬 Support

Got a suggestion, bug, or query related to the script? Don't hesitate to open an issue.

## 🤝 Contribution

Pull requests are a boon! For groundbreaking changes, it's best to open an issue first to discuss the proposed modifications.

## 📜 License

[MIT](https://choosealicense.com/licenses/mit/)
