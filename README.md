# 🌐 **OnionChains**

OnionChains is a meticulously crafted tool designed for the seamless creation and rotation of Tor configuration files. When paired with `proxychains`, it becomes a formidable force, ensuring that every single network request is dynamically routed through a unique Tor circuit.

---

## 🌟 **Features**

- **🛠️ Tor Configuration Generation**: Generate specified Tor configuration files with ease.
    
- **🔄 Dynamic ProxyChains Configuration**: Experience frictionless auto-configuration of proxychains, tailored for dynamic request handling.
    
- **🔓 Circumvent Internet Filters**: Navigate your network traffic through an array of Tor circuits, effortlessly bypassing filters and obstructions.
    
- **🔐 Backup Logging**: Safety takes precedence! Prior to any configuration changes, a backup is seamlessly generated.
    
- **🚪 Port Management**: Ports are meticulously managed by the script, ensuring availability and making necessary adjustments if they're in use.
    
- **🔍 Dependency Checks**: Before diving into execution, the script assesses the presence of essential tools like `tor` and `proxychains`, directing users towards installation if they're absent.
    
- **📜 Verbose Logging**: Elevate your debugging experience with the `--verbose` flag, ushering in detailed logging insights.
    

---

## 🚀 **Usage**

Dive deep into the vast array of command-line arguments and options `OnionChains` presents, enabling you to fine-tune its operations:

### 📜 **Command**:

`generate_proxychains [num_circuits] [OPTIONS]`

### 📌 **Arguments**:

- **num_circuits**:
    
    - **About**: Specifies the number of Tor circuits to generate, outlining the variety of paths your traffic can adopt through the Tor network.
    - **Example**:
    
    `generate_proxychains 3`
    

### 🔧 **Options**:

- **--proxychains-path**:
    
    - **About**: Pinpoint your `proxychains.conf` path. Defaults to `/etc/proxychains.conf`.
    - **Example**:
    
    `--proxychains-path="/path/to/your/proxychains.conf"`
    
- **--torrc-path**:
    
    - **About**: Define the destination directory for your `torrc` files. By default, it nestles in `/etc/tor`.
    - **Example**:
    
    `--torrc-path="/path/to/torrc/directory"`
    
- **--rotate-requests**:
    
    - **About**: Empower yourself to set the request threshold before ushering in a new Tor circuit rotation. By default, each request is unique in its circuit.
    - **Example**:
    
    `--rotate-requests=5`
    
    > 💡 Pro Tip: In the above, the circuit rotates every 5 requests.
    
- **--verbose**:
    
    - **About**: Flip on this switch for a rich, detailed logging panorama, shedding light on the script's operations.
    - **Example**:
    
    `--verbose`
    

### 🎯 **Examples**:

1. **Default Settings (3 Circuits)**:
    
    `generate_proxychains 3`
    
2. **Customized Behavior**:
    
    `generate_proxychains 5 --proxychains-path="/custom/path/proxychains.conf" --verbose`
    

---

## 🛠️ **Setup & Installation**

1. **🔄 System Update**:
    
    `sudo apt update`
    
2. **📦 Install Dependencies**:
    
    `sudo apt install tor proxychains python3-pip -y`
    
3. **🐍 Install Script Requirements**:
    
    `pip3 install click`
    
4. **🔧 Path Constants Configuration**: Default paths are `/etc/proxychains.conf` for `proxychains` and `/etc/tor` for `torrc` files. Customize using the `--proxychains-path` and `--torrc-path` flags, respectively.
    
5. **📜 Verbose Logging**: For a deeper dive into operations, toggle on the `--verbose` flag.
    

> 🚫 **Note**: Optimized for Ubuntu, this script calls for caution on other operating systems, especially where the cloak of anonymity is paramount.

---

## ⚠️ **Safety Considerations**

Venture wisely! Overutilizing chains may inadvertently betray your location due to anomalous network traffic patterns, potentially compromising your cloak of anonymity. For a balance of speed and security, a cap of 5 chains is advised.

---

## 🔑 **Permissions**

Accessing the `torrc` file necessitates the might of `sudo` permissions.

---

## 🎯 **Use Cases**

### 1. 🛡️ **Enhanced Anonymity in Network Scanning**

For the maestros of cybersecurity and penetration testing, OnionChains emerges as a sentinel, adding layers of anonymity to network scans. By directing `nmap` scans via diverse Tor circuits through `proxychains`, it masks their digital footprint, mitigating detection risks.


`proxychains sudo nmap -sT target_ip

### 2. 🌐 **Web Scraping with Rotating IPs**

Web scraping is a goldmine for developers and data aficionados. However, numerous web domains thwart recurrent requests by enforcing rate limits or IP bans. OnionChains ensures each request ventures through a unique Tor circuit, effectively wearing a new IP guise, bypassing such obstructions.

### 3. 🌍 **Circumventing Geo-restrictions**

Locked behind geographical content walls? Fret not! OnionChains facilitates users in accessing region-locked content by directing their network traffic through Tor circuits spanning diverse regions.

### 4. 🕵️ **Secure and Anonymous Browsing**

For netizens in regions riddled with internet censorship or heavy surveillance, OnionChains is their digital cloak, directing all browser traffic through a series of Tor circuits, granting unhindered access to restricted domains while curtailing surveillance threats.

---

## 🌐 **Accessing .onion Services with Mullvad Browser and OnionChains**

When married with OnionChains, the Mullvad browser holds the potential to unlock the mysteries of `.onion` services, allowing explorations into the depths of the "dark web", all the while ensconced in Mullvad's uniform fingerprinting shield.

📝 **Note**: While OnionChains lays down the pathway to `.onion` services via Tor circuits, it's pivotal to understand that the Tor Browser is handcrafted for `.onion` services, brimming with bespoke features and security protocols. If `.onion` realms are your primary hunting grounds, the Tor Browser remains unmatched. However, for those yearning for the melding of `.onion` access with Mullvad's consistent fingerprinting, this combination emerges as a potent alternative.

---

## 🏆 **Enhanced Anonymity with Mullvad Browser**

Mullvad isn't merely another name in the vast sea of VPN services. Birthed from a collaboration with the Tor Project, the Mullvad browser stands as a testament to their unyielding commitment to user privacy. This mutual endeavor ensures the browser is forged on a bedrock of profound expertise and an intricate understanding of the challenges encircling online anonymity.

The browser is architected with precision to unveil a singular feature: a consistent fingerprint. In today's digital age, where browser fingerprinting has burgeoned as a go-to technique for websites to discern and tail users, Mullvad emerges as a bastion, ensuring every user bears an identical digital signature, thwarting such tracking endeavors.

When synergized with OnionChains, Mullvad redefines the benchmarks of online anonymity:

- **🔍 Uniform Fingerprint**: Mullvad's alliance with the Tor Project assures its browser bestows a uniform fingerprint across its user base, making individual tracking an uphill battle.
    
- **🔄 Rotating IPs**: OnionChains enhances Mullvad's fingerprinting shield by intermittently rotating the user's IP. With traffic flowing through diverse Tor circuits, the origin of a request remains shrouded in mystery.
    

Together, they offer a comprehensive approach to online privacy, tackling both browser and network tracking mechanisms head-on.

---

## ❗ **Issues with OnionChains and Tor Browser**

Blending OnionChains with the Tor browser can concoct a potent mix, albeit with potential pitfalls:

1. **🔄 Double Tor Routing**: The Tor browser inherently treads the Tor network. Introducing OnionChains into the equation translates to a dual traverse through Tor, potentially hampering browsing velocities.
    
2. **⏱️ Amplified Latency**: The tandem can potentially inflate latency due to the addition of network relay points.
    
3. **🔍 Potential Overkill**: Both tools champion the cause of anonymity. Their concurrent use might render redundancy in many scenarios, possibly attracting unwanted scrutiny to your traffic.
    

Users are encouraged to judiciously weigh the advantages against the potential risks, ensuring a clear vision of the possible outcomes. Rigorous setup testing becomes paramount to sidestep inadvertent data leaks.

---

## 💬 **Support**

Encountered a suggestion, glitch, or have a query regarding the script? Your feedback is invaluable. Please, don't hesitate to [open an issue](https://chat.openai.com/c/bf79be82-f9d9-46da-908a-cb8f40e2a49b#).

---

## 🤝 **Contribution**

Pull requests are always welcome! For significant overhauls, it's prudent to [open an issue](https://chat.openai.com/c/bf79be82-f9d9-46da-908a-cb8f40e2a49b#) first, laying the groundwork for a discussion on the envisioned changes.

---

## 📜 **License**

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
