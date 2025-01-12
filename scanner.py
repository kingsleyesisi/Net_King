from utills.checkOS import check_os
import os 
import subprocess
import sys
import time

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
  
  # elif scannerOS == "linux":
    

scan_networks()