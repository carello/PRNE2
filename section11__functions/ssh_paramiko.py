import paramiko
import sys
from pprint import pprint

user = 'chet'
password = 'letmein'

cisco_command = "show ip route summary"

ip_address = '10.91.86.244'
username = user
password = password

print('--- Attempting connection to {}'.format(ip_address))

ssh_client = paramiko.SSHClient()

# Must set missing host key policy since we don't have the SSH key stored in the 'known_hosts' file
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Make the connection to our host.
try:
    ssh_client.connect(hostname=ip_address, username=username, password=password)
    # Execute some commands

except Exception as e:
    sys.stderr.write("\n--- SSH connection error: {} ---".format(e))


print('------------------------------------------------------\n')

stdin, stdout, stderr = ssh_client.exec_command(cisco_command)
data = [line.strip('\n') for line in stdout.readlines()]
for d in data:
    print(d)

ssh_client.close()
