# Networking Overview

---

# 1. What is a Computer Network?

A **computer network** is a collection of computers that can communicate and share resources.

Networks allow computers to:

- Share files
- Share printers
- Access the Internet
- Communicate with other devices

---

## Types of Networks

### LAN (Local Area Network)

A **LAN** connects computers in a small geographic area.

Examples:

- A building
- A group of buildings
- A university campus (e.g., HU campus)

---

### WAN (Wide Area Network)

A **WAN** connects computers over a large geographic area.

Examples:

- The Internet
- Connecting campuses in different cities
- Connecting offices across states or countries

> The Internet is the largest WAN in the world.

---

# 2. How Are Computers Connected?

## Wired Connections

### Twisted Pair Wire

- Similar to phone cable
- Often called:
  - *Ethernet cable* (refers to protocol)
  - *Cat 5 or Cat 6 cable* ("Category" refers to wire quality and twisting that affects signal distance and speed)

![Ethernet Cables](images/cat_5_cables.jpg)

---

### Coaxial Cable

- Used for cable television
- Older network type

![Coax Cable](images/coax.jpg)

---

### Fiber Optics

- Transmits **light**
- Not electrical current
- Very high speed and long distance

![Fiber Cables](images/fiber_options.jpg)
![Fiber Cables Close Up](images/fiber.jpg)

---

## Wireless Connections

- **Wi-Fi (802.11)**
- **Cellular wireless**
- **Satellite**

---

# 3. Network Hardware Devices

Computers on a network are connected using specialized devices.

## Router

- Connects **different networks**
- Directs traffic between your home network and the Internet
- Often assigns local IP addresses (via DHCP)

## Switch

- Connects devices within the same local network
- Sends data only to the correct destination device

## Modem

- Connects your home to your Internet Service Provider (ISP)
- Converts signals between your network and the provider’s network

---

# 4. Network Traffic

## Packet

A **packet** is a unit of data sent over a network.

Packets typically include:

- **Source address**
- **Destination address**
- **Data**
- **Error-checking information**

Large files are broken into many packets and reassembled at the destination.

![Network Packet Diagram](images/packets.png)

---

# 5. Network Addresses

## IP Address

An **IP address** identifies a device on a network.

Example:

```

199.8.89.29

```

---

## IPv4 (Internet Protocol Version 4)

- Stored in **4 bytes**
- Written as four numbers separated by dots
- Example:

```

199 . 8 . 89 . 29

```

---

## IPv6 (Internet Protocol Version 6)

- Uses **128 bits**
- Stored in **16 bytes**
- Designed to support many more devices

---

## Public vs Private IP Addresses

### Public IP Address

- Assigned by your ISP
- Visible on the Internet
- Must be unique worldwide

### Private IP Address

- Used inside your home or school network
- Not visible on the public Internet

Common private ranges:

- `192.168.x.x`
- `10.x.x.x`
- `172.16.x.x – 172.31.x.x`

Your router translates between private and public addresses using **NAT (Network Address Translation)**.

---

# 6. Domain Names and DNS

Computers translate **domain names** into **IP addresses**.

Example:

```

[www.huntington.edu](http://www.huntington.edu) → 199.8.89.29

```

---

## DNS (Domain Name System)

A **Domain Name Server (DNS)** translates domain names into IP addresses.

---

## Hostnames and Domain Names

A **hostname** or **domain name** identifies a computer on the Internet.

Examples:

- `www.huntington.edu`
- `euclid.huntington.edu`

---

## Top-Level Domains (TLDs)

The **TLD** is the last segment of a domain name.

Examples:

- `.edu`
- `.com`
- `.org`
- `.net`

---

## ICANN

**ICANN (Internet Corporation for Assigned Names and Numbers)** manages Internet domain names.

---

# 7. Static vs Dynamic Addresses

## Static IP Address

- Does **not change**
- Typically used by websites

## Dynamic IP Address

- Changes when connecting to the Internet
- Most personal devices use dynamic addresses

Try this:

- Open a browser
- Search: `"what is my ip"`

---

# 8. How the Internet Works (Simplified)

When you visit a website:

1. You enter a URL into your browser.
2. DNS translates the domain name into an IP address.
3. Your computer sends packets to that IP address.
4. Routers move the packets across multiple networks.
5. The server responds with web page data.
6. Your browser reassembles the packets and displays the page.

---

# 9. Protocols

Communication over a network must follow **protocols**.

A **protocol** is a set of rules that govern how messages are sent and received.

---

## TCP/IP

**TCP/IP (Transmission Control Protocol / Internet Protocol)**  
The core protocol used by computers on the Internet.

---

## Port Numbers

IP addresses identify a computer.

**Port numbers identify a specific service on that computer.**

Examples:

- HTTP → Port 80
- HTTPS → Port 443
- FTP → Port 21
- SSH → Port 22

---

## TCP/IP Utilities

### `ping`

- Tests whether a destination is reachable
- Can be used to find the DNS entry for an address

![Ping Example](images/ping.png)

---

### `tracert` (Trace Route)

- Shows the route a packet takes to reach a destination

![Tracert Example](images/tracert.png)

---

# 10. High-Level Protocols

These protocols build on TCP/IP.

---

## FTP (File Transfer Protocol)

- Transfers files between computers

---

## Telnet and SSH

- Allow users to log into a remote computer
- SSH is secure

---

## HTTP (Hypertext Transfer Protocol)

- Defines how web pages are exchanged

---

## URL (Uniform Resource Locator)

A **URL** defines a resource on the Internet.

Example:

```

[http://www.huntington.edu](http://www.huntington.edu)

```

---

## HTTPS

The **"S"** in HTTPS means:

> **Secure connection**

HTTPS uses encryption to protect:

- Passwords
- Credit card numbers
- Personal data

Without HTTPS, data could potentially be intercepted while traveling across the network.

---

# 11. Network Layers (Simplified)

Networking is organized into layers.

Examples:

- **Physical Layer** – cables, fiber, wireless signals  
- **Network Layer** – IP addressing and routing  
- **Transport Layer** – TCP (reliable delivery)  
- **Application Layer** – HTTP, FTP, SSH  

Each layer has a specific responsibility in network communication.
```

---

