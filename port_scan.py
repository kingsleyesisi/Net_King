import socket 
import time 
import subprocess 
import os
import sys



start_time = time.time()
def scan_ports(target, start_port, end_port):
  print(f"Scanning target {target} from port {start_port} to {end_port}")
  for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.001)
    result = sock.connect_ex((target, port))
    addr_info = socket.getaddrinfo(target, port)
    for addr in addr_info:
      print(f"Address info: {addr}")
    if result == 0:
      print(f"Port {port}: Open")
    sock.close()
end_time = time.time()
print(time.strftime("%H:%M:%S", time.gmtime(end_time - start_time)))

if __name__ == "__main__":
  target = '127.0.0.1'
  start_port = int(1)
  end_port = int(1000)
  start_time = time.time()
  scan_ports(target, start_port, end_port)
  end_time = time.time()
  print(time.strftime("%H:%M:%S", time.gmtime(end_time - start_time)))
  print(f"This is the run time of the function: {end_time - start_time}")