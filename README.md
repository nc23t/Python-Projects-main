# scannerMan — Simple TCP/UDP Port Scanner (Python)

A small learning-focused port scanner written in Python. It supports IPv4 input validation, TCP connect scans, basic UDP probing, and interactive prompts so you can test quickly on your own network.

---

## Features
- TCP **connect scan** over a **single host** or an **IP range**
- Scan a **port range** (e.g., 1–1024) or a **custom list** (e.g., 22,80,443)
- **UDP probe** (send a small datagram and wait briefly for a reply)
- **IPv4 validation** using Python’s `ipaddress` module
- **Global socket timeout** so scans don’t hang
- Minimal dependencies (Python standard library only)

---

## Requirements
- Python 3.9+ (works with standard library only)
- A network you own or have permission to test

*(Ethics & legal: only scan systems you are authorized to scan.)*

Disclaimer
This project is for educational use. Scan only hosts/networks you have explicit permission to test.
