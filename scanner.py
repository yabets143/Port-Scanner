import socket 
import threading
from queue import Queue
import argparse
import time
from tqdm import tqdm
import ipaddress
import subprocess

parser = argparse.ArgumentParser(description="A simple port scanner script to scan a target's open ports and optionally scan a subnet for live hosts.")

parser.add_argument("target", help="The target IP address or domain name to scan for open ports. Example: 'scanme.nmap.org' or '192.168.1.1'")
parser.add_argument("-t","--thread",type=int, help="The number of threads to use for port scanning. Example: '-t 200'. Default is 300 if not provided.", required=False,default=200)
parser.add_argument("-r","--range", type=int, help="The maximum number of ports to scan. Example: '-r 500'. Default is 1000 if not provided.", required=False,default=1000)
parser.add_argument("-s", "--subnet", help="Scan the subnet for live hosts (CIDR format) Example: '-s 192.168.1.0/24'.", required=False)
args =  parser.parse_args()

start_time = time.time()
target=args.target 
ranges=args.range 
queue = Queue()
open_ports = []
threads_to_run=args.thread

#progress_bar = tqdm(total=ranges, desc="Scanning Ports", unit="port")
progress_bar = tqdm(total=ranges,desc="Scanning", position=0,unit="port")

def scanport(port):
 try:
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock.settimeout(2)
  sock.connect((target, port))
  sock.close()
  return True
 except:
  return False

def fill_queue(port_list):
 for port in port_list: 
  queue.put(port)

def worker():
 while not queue.empty():
  port = queue.get()
  if port is None:
   break
  if scanport(port):
   sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   sock.connect((target, port))
   sock.settimeout(2)
   service = socket.getservbyport(port)
   print(f"\n\n[+] port {port}/{service} is open\n")
   open_ports.append(port)
  progress_bar.update(1)
  queue.task_done()

# Scan live hosts in the subnet
def scan_subnet(subnet):
    """Scan a subnet for live hosts."""
    live_hosts = []
    net = ipaddress.IPv4Network(subnet, strict=False)
    print(f"Scanning subnet {subnet} for live hosts...")
    for ip in net.hosts():
        ip_str = str(ip)
        response = subprocess.run(["ping", "-c", "1", "-W", "1", ip_str], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            print(f"Host {ip_str} is live.")
            live_hosts.append(ip_str)
    print("\nLive hosts found:", live_hosts)
    return live_hosts

# If subnet scanning is provided, run it
live_hosts = []
if args.subnet:
    live_hosts = scan_subnet(args.subnet)

# Prepare the queue for port scanning
if not live_hosts:  # If no subnet is specified, scan the provided target
    live_hosts = [target]
port_list = range(ranges)
fill_queue(port_list)
with tqdm(total=ranges, desc="Scanning Ports", position=0, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]") as progress_bar:
 thread_list = []
 for t in range(threads_to_run):
  thread = threading.Thread(target=worker)
  thread_list.append(thread)
  thread.start()

 queue.join()

 for _ in range(threads_to_run):
     queue.put(None)

#for thread in thread_list:
# thread.start()

# wait for all threads to complete
 for thread in thread_list:
  thread.join()
 progress_bar.clear()
# progress_bar.close()
end_time = time.time()
elapsed_time = end_time - start_time
print("\n\nopen ports are: ", open_ports)
print(f"excution time{elapsed_time:.2f} seconds")
