from utills.checkOS import check_os
from utills.runtime import runtime

import os 
import subprocess
import sys
import socket


# Scan a website for it's IP address

def WebIPScan(url, *agr, **kwagr):
  wurl = (url, 80)
  scan = socket.getaddrinfo("example.org", 80, proto=socket.IPPROTO_TCP)
  return scan


@runtime
def WifiScan():
  """
  Scan for available WiFi networks for different operating system 
  either windows or Linux operating system. 
  this function determines the operating system and runs the appropriate command 
  to list available WiFi networks. For windows, it uses the 'netsh' command to 
  show networks. For Linux it uses the Airmon-ng.

  Args: 
        None.

  Returns: 
        str: A string containing the list of available WiFi networks and info about the network

  
  """
  scannerOS = check_os()
  if scannerOS == "windows":
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
    return result
  
  elif scannerOS == "linux":
    try:
      result = subprocess.run(["ip", "addr", "show"], capture_output=True, text=True).stdout

      if "wlan" or 'wlan0' in result:
        return "Discovered wireless Interface in this device"
      else:
        return "No Wireless Interface Detected"
      
    except Exception as e:
      return e
    

if __name__ == '__main__':
  url = 'google.com'
  result = WebIPScan(url)
  print(result)