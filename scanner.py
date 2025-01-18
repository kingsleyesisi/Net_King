from utills.checkOS import check_os
from utills.runtime import runtime

import os 
import subprocess
import sys


@runtime
def scan_networks():
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
  test_function = scan_networks()
  print(test_function)