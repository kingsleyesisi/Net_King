import nmap
import time
import threading
import os
import sys
import time 

# Check which operating system  is running on either windows, mac or linux 
def check_os():
    """ 
    Checking the operating system of the User for smooth experience 

    Args:
        None
    Returns:
        str: The operating system of the user.
    Example:
        check_os()
        This will return the operating system of the user.
        => 'windows'
        => 'linux'
        => 'mac'

    """

    if os.name == 'nt':
        return 'windows'
    elif os.name == 'posix':
        return 'linux'
    else:
        return 'mac'
UserOS = check_os()

def scan_ip(base_ip, port_range: str = '5000'):
    """ 
    It takes in one argument which is the base IP address (e.g., 192.168.)
    and completes the rest of the IP address range to scan.

    Args:
        base_ip(str): The base IP address to scan (e.g., '192.168').
        port_range (str, optional): The range of ports to scan. Defaults to '5000'.
    Returns:
        None
        Results are printed to the console.
    Example:
        scan_ip('192.168')
        This will scan all IP addresses from 192.168.0.0 to 192.168.255.255
        and check the status of the ports in the specified range.
    """
    last_numb = [i for i in range(0, 256)]
    Third_numb = range(0, 256)
    try:
        nm = nmap.PortScanner()

    except nmap.PortScannerError:
        print('Nmap not found in this system', sys.exc_info()[0])
        
        """ Download and install nmap if not found in the system """
        from download import download_and_install_nmap
        download_and_install_nmap(UserOS)

    # Generating the IP address last digits and scanning the IP address
    for Third in Third_numb:
        for Last in last_numb:
            GateWay = f'{base_ip}.{Third}.{Last}'
            
            # Scanning for open ports
            nm.scan(GateWay, port_range) 
            if nm[GateWay].state() == 'up':
                print(f'Host : {GateWay} ({nm[GateWay].hostname()}) is up')

            for proto in nm[GateWay].all_protocols():
                lport = nm[GateWay][proto].keys()
                for port in lport:
                    print(f'Host : {GateWay} ({nm[GateWay].hostname()})')
                    print(f'Port : {port}\tState : {nm[GateWay][proto][port]["state"]}')
    return nm

# Check Run Time of the function 
def run(base_ip):
    start_time = time.time()
    scan_ip(base_ip)
    end_time = time.time()
    # print(f'Runtime: {end_time - start_time} seconds')

run('192.168')
