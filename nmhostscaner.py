import nmap
import time
import threading
import os
import time 


# Check which operating system  is running on either windows, mac or linux 
def check_os():
    """ 
    Checking the operating system of the User for smooth experience 
    """

    if os.name == 'nt':
        return 'windows'
    elif os.name == 'posix':
        return 'linux'
    else:
        return 'mac'

UserOS = check_os()

def scan_ip(base_ip, port_range: str = '2000'):
    """ 
    This function allows you to scan a range of IP addresses
    and check the status of the ports on the IP addresses.
    
    it takes in one argument which is the base Ip address e.g. (192.168)
    and it completes the rest 

    """

    nm = nmap.PortScanner()
    last_numb = [i for i in range(0, 256)]
    Third_numb = range(0, 256)

    # Generating the IP address last digits and scanning the IP address
    for Third in Third_numb:
        for Last in last_numb:
            GateWay = f'{base_ip}.{Third}.{Last}'
            
            # Scanning base on the port range so any port can be used 
            # based on the user input

            nm.scan(GateWay, port_range) 
            if nm[GateWay].state() == 'up':
                print(f'Host : {GateWay} ({nm[GateWay].hostname()}) is up')

            for proto in nm[GateWay].all_protocols():
                lport = nm[GateWay][proto].keys()
                for port in lport:
                    print(f'Host : {GateWay} ({nm[GateWay].hostname()})')
                    print(f'Port : {port}\tState : {nm[GateWay][proto][port]["state"]}')


# Check Run Time of the function 
def run(base_ip):
    start_time = time.time()
    scan_ip(base_ip)
    end_time = time.time()
    print(f'Runtime: {end_time - start_time} seconds')

run('192.168')
