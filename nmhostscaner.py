import nmap
import time



def Host_IP_Addr():
    Third_numb = [i for i in range(1,1000)]
    Last_numb = [i for i in range(1,1000)]

    Third_digit = 0 
    Last_digit = 0

    for Third in Third_numb:
        Third_digit =+ Third
        for Last in Last_numb:
            Last_digit =+ Last
            host = f'192.168.{Third_digit}.{Last_digit}'
            # print(host)

def run(Host_IP_Addr):
    start_time = time.time()
    Host_IP_Addr()
    end_time = time.time()
    print(f'Runtime: {end_time - start_time} seconds')

run(Host_IP_Addr)