import paramiko
import sys


# Defining Child Classes
# Define a base class for a generic network device, and will define child classes
# for specific device types:IOS and IOS-XR. The main functionality for this lab
# will be to implement connect and get_interfaces methods for your child classes.

# PART 1: Defining Child Classes
# Define a base network device class with the usual attributes for name,
# IP, username, and password. Your base class will have an empty connect
# method that sets the session attribute to None, and a get_interfaces method
# that returns a string such as "Base device, cannot get interfaces".

print('\n--- Part 1 ---')
print()


class NetworkDevice(object):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.interfaces = ''

    def connect(self):
        self.session = None


    def get_interfaces(self):
        self.interfaces = "Base device, cannot get interfaces"


# Define child device-specific classes for IOS and IOS-XR device types.
# For your IOS class, your connect method will actually connect to the device,
# storing the session as an attribute. Your get_interfaces method will run the show int brief command on the device,
# and will store the output.
#
# For your IOS-XR class, you will create 'stub' methods for both connect and get_interfaces.
# The connect method will set the session to None, and the get_interfaces method will return a string saying
# "Getting interface information a different way", to simulate the behavior of different object types satisfying
# requests in a device-specific manner.

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

