import os 
import sys
import getpass
import subprocess as sp
from utills.runtime import runtime

class LinuxPass:
    def __init__():
        # Get the username
        username = getpass.getuser()
        return username
    
    def Password(username):
        user = username
        path2 = '/etc/shadow'
        path2 = '/etc/passwd'
        system = sp.run(["sudo", "cat", path2], capture_output=True, text=True).stdout
        return system

if __name__ == "__main__":
    run = LinuxPass.Password('kingsleyesisi')
    print(run)