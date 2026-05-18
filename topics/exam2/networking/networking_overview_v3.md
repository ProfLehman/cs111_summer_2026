# Networking & Internet Overview

---

# 1. Basic Network Concepts

## What is a Computer Network?

A **computer network** is a collection of computers that can communicate and share resources.

---

## Client/Server Model

In the **client/server model**:

- **Client computers** request resources.
- **Server computers** provide resources.

### Types of Servers

- **Web server** – delivers web pages
- **File server** – stores and shares files
- **Print server** – manages printers

---

## LAN (Local Area Network)

A **LAN** connects computers in a small geographic area.

Examples:

- A building
- A group of buildings
- A university campus

---

### WAN (Wide Area Network)

A **WAN** connects computers over a large geographic area.

Examples:

- The Internet
- Connecting campuses in different cities
- Connecting offices across states or countries

> The Internet is the largest WAN in the world.

---

## Router

A **router**:

- Connects different networks
- Directs packets between your local network and the Internet
- Often connects your home network to your ISP

---

# 2. Network Traffic

## Packet

A **packet** is a unit of data sent over a network.

Packets typically include:

- Source address
- Destination address
- Data

Large files are broken into many packets and reassembled at the destination.

![Network Packet Diagram](images/packets.png)

---

# 3. Connections

Computers connect using wired or wireless technologies.

---

## Twisted Pair (Ethernet Cable)

- Common home and office network cable
- Often called **Cat 5 or Cat 6**
- Uses the **Ethernet** protocol

![Ethernet Cables](images/cat_5_cables.jpg)

---

## Coaxial Cable

- Used for cable television and Internet service

![Coax Cable](images/coax.jpg)

---

## Fiber Optics

- Transmits data using **light**
- Very fast and long distance

![Fiber Cables](images/fiber_options.jpg)
![Fiber Cables Close Up](images/fiber.jpg)

---

## Wireless

- **Wi-Fi**
- **Cellular**
- **Satellite**

---

# 4. ISP and Broadband

## ISP (Internet Service Provider)

An **ISP** connects your home or school network to the Internet.

Examples: cable companies, fiber providers, cell providers.

---

## Broadband

**Broadband** means high-speed Internet access that is always on.

Examples:

- Cable Internet (coax cable)
- Fiber Internet (fiber optic cable)
- DSL (traditional copper phone lines)

---

# 5. Protocols

A **protocol** is a set of rules that govern communication between computers.

---

## Ethernet

Used for communication on local wired networks (LANs).

---

## TCP/IP

**TCP/IP (Transmission Control Protocol / Internet Protocol)**  
The core protocol used on the Internet.

- IP handles addressing.
- TCP ensures reliable delivery of data.

---

# 6. Internet History

- **1969** – ARPANET [early Internet](https://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~369647~90137022:First-Maps-of-the-Internet) begins.
- **1990s** – The **World Wide Web** becomes popular.

The Internet is the global network of networks.  
The World Wide Web is a service that runs on the Internet.

---

# 7. Addressing and Naming

## IP Address

An **IP address** identifies a device on a network. Each address uses
four numbers where each number is a byte thus 0 to 255.

Example:

**199.8.89.29**
---

## Domain Name

A **domain name** is a human-readable name for a computer.

Example:

**http://www.huntington.edu**  

**http://google.com**


## Top-Level Domains (TLDs)

The **TLD** is the last segment of a domain name.

Examples:

- `.edu`  Education
- `.com`  Commercial
- `.org`  Non-Profit
- `.ca`   Canada
- `.de`   Germany (why?)

---

## DNS (Domain Name System)

**DNS** translates domain names into IP addresses. The DNS serves as and address book for web
site domain names.r 

Example:

Web address **http://www.huntington.edu** translates to IP address **199.8.89.29**


---

## URL (Uniform Resource Locator)

A **URL** identifies a specific resource on the Internet.

Example:

```
http://www.huntington.edu
```

---

## HTTP and HTTPS

**HTTP (Hypertext Transfer Protocol)** defines how web pages are transferred between browsers and web servers.


The **"S"** in HTTPS means:

> **Secure connection**

HTTPS uses encryption to protect:

- Passwords
- Credit card numbers
- Personal data

Without HTTPS, data could potentially be intercepted while traveling across the network.


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

# 9 TCP/IP Utilities

Use the **command line** ie. **terminal** on your computer to run the following commands.


### Finding your IP address

Type `ifconfg` (Mac) or `ipconfig` (Windows) to see your IP address.



### `ping`

- Tests whether a destination is reachable
- Can be used to find the DNS entry for an address

![Ping Example](images/ping.png)

---

### `tracert` (Trace Route)

- Shows the route a packet takes to reach a destination

![Tracert Example](images/tracert.png)

---

# 10 ilight network

Huntington University uses the iLight netwwork to connect to the Internet.

See [ilight network map](https://ilight.net/ilight-map.html)

See [Traffic Stats](https://ilight.net/member-portal/)

![HU IHETS Traffic for Year](images/hu_ihets_year.png)

-- end --

