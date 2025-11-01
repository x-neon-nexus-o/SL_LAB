# Nmap on Fedora — Quick README

This README provides a compact, copy-paste friendly set of Nmap installation and usage commands tailored for **Fedora**.

> **Prerequisite:** Run commands that require raw packet access with `sudo`, or grant capabilities to the `nmap` binary (example shown below).

---

## 1. Install Nmap

```bash
sudo dnf update -y
sudo dnf install nmap -y
```

---

## 2. Version detection

```bash
nmap -sV <target-host-or-IP>
```

---

## 3. Scan by hostname and by IP

```bash
# Hostname
nmap www.geeksforgeeks.org

# IP address
nmap 172.217.27.174
```

---

## 4. Verbose output

```bash
nmap -v www.geeksforgeeks.org
```

---

## 5. Scan multiple hosts

```bash
nmap 103.76.228.244 157.240.198.35 172.217.27.174
```

---

## 6. Scan a whole subnet

```bash
# Wildcard (less recommended)
nmap 103.76.228.*

# Preferred: CIDR
nmap 103.76.228.0/24
```

---

## 7. Scan a specific IP range

```bash
nmap 192.168.29.1-20
```

---

## 8. Detect firewall settings (ACK scan)

```bash
sudo nmap -sA 103.76.228.244
```

---

## 9. TCP SYN (stealth) scan

```bash
sudo nmap -sS <domain-or-IP>
```

---

## 10. Ping scan and UDP scan

```bash
# Ping scan (no port scan)
nmap -sn <domain-or-IP>

# UDP scan (usually requires sudo)
sudo nmap -sU <domain-or-IP>
```

---

## 11. Scan specific ports

```bash
nmap -p 80,443,21 <domain-or-IP>
```

---

## 12. Scan a range of ports

```bash
nmap -p 1-80 <domain-or-IP>
```

---

## 13. Aggressive scan (OS, version, scripts, traceroute)

```bash
sudo nmap -A <domain-or-IP>
```

---

## 14. Traceroute

```bash
nmap --traceroute <domain-or-IP>
```

---

## 15. OS detection

```bash
sudo nmap -O <domain-or-IP>
```

---

## Grant capabilities (optional — run without `sudo`)

If you prefer not to run `nmap` with `sudo`, grant the binary the capabilities required for raw network access:

```bash
# Install libcap utilities if needed
sudo dnf install libcap -y

# Grant capabilities to nmap so raw socket scans work without sudo
sudo setcap cap_net_raw,cap_net_admin+eip $(which nmap)
```

> Note: Granting capabilities is a security-sensitive action — understand the implications before applying on multi-user systems.

---

## Tips

* Prefer CIDR notation (`/24`) when scanning full networks.
* Use `sudo` for raw-packet scans (SYN, ACK, OS detection, UDP) if you haven't applied capabilities.
* Be mindful of legal and ethical considerations: obtain permission before scanning networks you don't own.

---

## Quick cheat-sheet (one-liners)

```bash
# Install
sudo dnf install nmap -y

# SYN scan (stealth)
sudo nmap -sS target.com

# Version detection
nmap -sV target.com

# Ping-only
nmap -sn 192.168.1.0/24

# UDP scan
sudo nmap -sU target.com

# Aggressive
sudo nmap -A target.com
```

---

## License

This README is provided as-is for educational purposes. Use responsibly.


# Network Commands — README.md

This README explains common network diagnostic and lookup commands found on Unix-like systems, with short descriptions and **examples** you can copy-paste.

> Note: On many modern Linux distributions `ifconfig` is deprecated in favor of the `ip` command from the `iproute2` package. Examples for both are provided.

---

## ifconfig / ip

**Description:** `ifconfig` configures and displays network interface parameters. Many systems now use `ip` instead.

**Examples:**

```bash
# Show all interfaces (ifconfig)
ifconfig -a

# Show all interfaces (ip equivalent)
ip addr show

# Bring interface up (ifconfig)
sudo ifconfig eth0 up

# Bring interface up (ip)
sudo ip link set dev eth0 up

# Assign IP address (ifconfig)
sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0

# Assign IP address (ip)
sudo ip addr add 192.168.1.10/24 dev eth0
```

---

## whois

**Description:** Query WHOIS databases for domain, IP, and registrar information.

**Examples:**

```bash
# Query domain registrar info
whois example.com

# Query WHOIS for an IP address
whois 8.8.8.8
```

---

## dig

**Description:** DNS lookup utility to query DNS servers for records (A, AAAA, MX, TXT, etc.).

**Examples:**

```bash
# Lookup A record
dig example.com A

# Query specific nameserver
dig @8.8.8.8 example.com

# Show short answer (one-line)
dig +short example.com

# Query MX records
dig example.com MX
```

---

## ping

**Description:** Test reachability of a host and measure round-trip time using ICMP echo requests.

**Examples:**

```bash
# Ping until stopped (Ctrl+C)
ping example.com

# Ping 5 times and stop
ping -c 5 example.com
```

---

## traceroute

**Description:** Shows the route packets take to reach a destination and where latency accumulates.

**Examples:**

```bash
# IPv4 traceroute
traceroute example.com

# Use ICMP instead of UDP (may require sudo)
traceroute -I example.com

# IPv6 traceroute
traceroute -6 example.com
```

---

## nslookup

**Description:** Interactive and non-interactive DNS query tool to get DNS records and debug DNS.

**Examples:**

```bash
# Non-interactive lookup
nslookup example.com

# Use a specific DNS server
nslookup example.com 8.8.8.8

# Interactive mode
nslookup
> server 8.8.8.8
> set type=MX
> example.com
> exit
```

---

## netstat

**Description:** Displays active network connections, routing tables, interface stats. Note: `netstat` comes from the `net-tools` package and is deprecated on many systems in favor of `ss` and `ip`.

**Examples:**

```bash
# Display all active connections and listening ports
netstat -a

# Show active udp and tcp connections
netstat -ut

# Show only UDP connections
netstat -u

# Show kernel IP routing table
netstat -r

# Show fully qualified domain names for remote addresses (if supported)
netstat -f
```

**Alternative (modern):**

```bash
# Similar to netstat -a
ss -a

# Show TCP and UDP sockets
ss -t -u -a

# Show routing table (ip route)
ip route show
```

---

## Installing missing tools (common packages)

```bash
# On Debian/Ubuntu
sudo apt update && sudo apt install -y net-tools dnsutils bind9-dnsutils whois traceroute

# On Fedora
sudo dnf install -y net-tools bind-utils whois traceroute
```

---

## Tips & Notes

* Always run network diagnostic tools with appropriate permissions.
* Be cautious when scanning or querying resources you don't own; obtain permission.
* Prefer modern equivalents (`ip`, `ss`, `dig`) where available for more features and active maintenance.

---

> This README provides practical examples — copy the commands into your terminal to try them out.


#include <stdio.h>
#include <string.h>

int main(void) {
    char buff[17];
    int pass = 0;

    printf("Enter the password: ");
    if (fgets(buff, sizeof buff, stdin) == NULL) {
        fprintf(stderr, "Input error\n");
        return 1;
    }

    /* remove trailing newline if present */
    buff[strcspn(buff, "\n")] = '\0';

    if (strcmp(buff, "thecorrectpaswd") == 0) {
        puts("Correct Password");
        pass = 1;
    } else {
        puts("Wrong Password");
    }

    if (pass) {
        puts("Root privileges given to the user");
        /* privileged actions go here */
    }

    return 0;
}