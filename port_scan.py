import socket 
import subprocess 
import os
import sys
from utills.runtime import runtime

@runtime
def scan_ports(target, start_port, end_port):
  print(f"Scanning target {target} from port {start_port} to {end_port}")
  for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((target, port))
    # print(result)
    addr_info = socket.getaddrinfo(target, port)
    if result == 0:
      print(f"Port {port}: Open")
      print(f"Address Info: {addr_info}")
    if result == 0:
      print(f"Port {port}: Open")
    sock.close()
    if result == 111:
      raise ConnectionError
    # elif result == 101:
    #   raise BufferError


if __name__ == "__main__":
  target = '100.115.92.207'
  start_port = int(1)
  end_port = int(1000)
  scan_ports(target, start_port, end_port)