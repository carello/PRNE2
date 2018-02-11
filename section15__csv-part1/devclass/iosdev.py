import paramiko
import sys
from devclass.basedev import NetworkDevice


class NetworkDeviceIOS(NetworkDevice):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)

    def connect(self):
        print('--- Attempting connection to {}'.format(self.ip_address))
        ssh_client = paramiko.SSHClient()

        # Must set missing host key policy since we don't have the SSH key stored in the 'known_hosts' file
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Make the connection to our host.
        try:
            ssh_client.connect(hostname=self.ip_address, username=self.username, password=self.password)
            # Execute some commands
        except Exception as e:
            sys.stderr.write("\n--- SSH connection error: {} ---".format(e))

        # TEST LOCALLY
        #stdin, stdout, stderr = self.session.exec_command('show ip interface brief')
        #data = [line.strip('\n') for line in stdout.readlines()]
        #print('-- IN GET INTERFACES ---')
        #for d in data:
        #    print(d)
        self.session = ssh_client



    def get_interfaces(self):
        stdin, stdout, stderr = self.session.exec_command('show ip interface brief')
        #data = [line for line in stdout.readlines()]
        self.interfaces = stdout

