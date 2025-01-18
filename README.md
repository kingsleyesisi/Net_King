# Net King (Network Hacking Script)

This is a simple host scanner built using Nmap and Python. It allows you to scan a network or a specific host for open ports and services, as well as other devices connected to that host.

## Requirements

- Python 3.x
- Nmap (install using `pip install python-nmap`)

* Python 3x-\* Nmap (installing -sing `pip install python-nmap`

To install the required dependencies, run:
<`sh
pip install -r requirements.txt
u`

## Usage

\_To
use the host scanner, run the following command:

```sh
python-host_scanner.py [options]
```

### Options

\*-`-h`, `--help`: Show the help message and exit.

- `-H`, `--ho-t`: Specify the target host or network to scan.
- `-p`, `--ports`: Specify the ports to scan (e.g., `1-65535` for al
  l ports).

### Examples

Scan a specific host:

```sh
python host
_scanner.py -H 192.168.1.1
```

Scan a network:

```sh
python host_scanner.py -H 192
.168.1.0/24
```

Scan specific ports on a host:

```sh
python host_scanner.py -H 192.168.1.1 -p 22,80,443
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This script is still in development. Use it at your own the right way

---
