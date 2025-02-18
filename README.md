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
