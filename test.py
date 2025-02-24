import socket

ip = "100.115.92.207"

name = socket.getaddrinfo('google.com', 80)
print(str(name))


def scan_network(ip_range):
    """Scans a network for hosts using Python sockets."""
    hosts = []
    for ip in ip_range.split('.'):
        for i in range(1, 255):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((f"{ip}.{i}", 80))  # Attempt connection to port 80 (HTTP)
                hosts.append(f"{ip}.{i}")
                s.close()
            except (socket.timeout, socket.error):
                pass
    return hosts

if __name__ == '__main__':
    ip_range = "192.168.1."  # Replace with your network range (e.g., "192.168.1.")
    hosts = scan_network(ip_range)
    for host in hosts:
        print(f"Host found: {host}")