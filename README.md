# Port Scanner

A simple Python-based port scanner script that allows you to scan open ports on a target host and optionally scan a subnet for live hosts.

## Features

- Scan a target IP address or domain name for open ports.
- Customize the number of threads to speed up scanning.
- Optionally, scan a subnet for live hosts.
- Supports scanning up to a configurable range of ports.
- Outputs open ports and their associated services.
- Progress bar to track scanning progress.

## Requirements

- Python 3.x
- Libraries:
  - `socket` (default, no installation required)
  - `threading` (default, no installation required)
  - `queue` (default, no installation required)
  - `argparse` (default, no installation required)
  - `time` (default, no installation required)
  - `tqdm` for the progress bar (install via `pip install tqdm`)
  - `subprocess` for subnet scanning (default, no installation required)
  - `ipaddress` for subnet scanning (default, no installation required)

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
```

### Install dependencies:

```python
pip install tqdm
```
##### Usage
```bash
python port_scanner.py <target> [options]
```
#### Arguments:
  - target (required): The IP address or domain name to scan. Example: scanme.nmap.org or 192.168.1.1.
  - -t or --thread (optional): The number of threads to use for scanning (default is 200).  
  - -r or --range (optional): The maximum number of ports to scan (default is 1000).
  - -s or --subnet (optional): Scan a subnet for live hosts in CIDR format. Example: 192.168.1.0/24.
Example Commands:
Scan a single target:
```bash
python port_scanner.py 192.168.1.1
```
Scan a target with a custom range of ports:
```bash
python port_scanner.py 192.168.1.1 -r 500
```
Scan a subnet for live hosts and scan open ports on them:

```bash
python port_scanner.py 192.168.1.1 -s 192.168.1.0/24
```
Scan with more threads to speed up the process:

```bash
python port_scanner.py 192.168.1.1 -t 500
```
Output
The script will display:

A progress bar indicating the current status of the scan.
Open ports along with their associated services (e.g., HTTP, FTP).
The list of live hosts (if subnet scanning is enabled).
Execution time of the scan.
Example Output:
```kotlin
Scanning subnet 192.168.1.0/24 for live hosts...
Host 192.168.1.1 is live.
Host 192.168.1.2 is live.

Live hosts found: ['192.168.1.1', '192.168.1.2']

Scanning 1000 ports for target 192.168.1.1...

[+] port 22/ssh is open
[+] port 80/http is open

open ports are: [22, 80]
execution time: 2.35 seconds
```
