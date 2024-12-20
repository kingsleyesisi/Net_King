import nmap
import time


last_numb = [i for i in range(0, 256)]

def scan_ip(base_ip):
    nm = nmap.PortScanner()
    Third_numb = range(0, 256)
    for Third in Third_numb:
        for Last in last_numb:
            host = f'{base_ip}.{Third}.{Last}'
            # print(host)

def run(base_ip):
    start_time = time.time()
    scan_ip(base_ip)
    end_time = time.time()
    print(f'Runtime: {end_time - start_time} seconds')

run('192.168')
