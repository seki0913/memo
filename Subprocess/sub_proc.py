import subprocess

from netaddr import *

IP = "192.168.10.235"
Sub = "255.255.255.0"

Subnet = str(IPAddress(Sub).netmask_bits())


# PowerShell の設定を実行許可に変える

cmd = "powershell -ExecutionPolicy RemoteSigned -File ./network_config.ps1 "+ IP + " " + Subnet
returncode = subprocess.call(cmd)