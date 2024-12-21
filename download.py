import subprocess
import os

def download_and_install_nmap(UserOS):
    """ 
    This function downloads the Nmap installer and installs it on the user's machine.
    The installer is downloaded from the official Nmap website.
    The installer is saved as 'nmap-setup.exe' in the current directory.
    The installer is run with the '/S' flag to install Nmap silently.
    """
    if UserOS == 'windows':
        # URL to download Nmap installer
        nmap_url = "https://nmap.org/dist/nmap-7.91-setup.exe"
        installer_path = "nmap-setup.exe"

        # Download the Nmap installer using aria2c for faster download
        nmap_url = "https://nmap.org/dist/nmap-7.91-setup.exe"
        installer_path = "nmap-setup.exe"

        # Download the Nmap installer
        subprocess.run(["curl", "-L", "-o", installer_path, nmap_url], check=True)

        # Run the installer
        subprocess.run([installer_path, "/S"], check=True)

        # Clean up the installer file
        os.remove(installer_path)

        # Install Nmap using the package manager
    elif UserOS == 'linux':
        subprocess.run(["sudo", "apt-get", "install", "nmap"], check=True)

        # Install Nmap using Homebrew
    elif UserOS == 'mac':
        subprocess.run(["brew", "install", "nmap"], check=True)

if __name__ == "__main__":
    download_and_install_nmap()