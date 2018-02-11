import paramiko
import sys
from pprint import pprint

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


# Create a function to read in the 'challenge-devices' file, creating and returning the list of device objects,
# created as appropriate for each IOS, IOS-XR, and generic device in the file.

def read_device(devices_file):
    devices2_list = list()

    with open(devices_file, 'r') as f:
        device_info = [line.strip().split(',') for line in f.readlines()]

        for d in device_info:
            if d[1] == 'ios':
                device2 = NetworkDeviceIOS(d[0], d[2], d[3], d[4])

            elif device_info[1] == 'ios-xr':

                device2 = NetworkDeviceXR(d[0], d[2], d[3], d[4])

            else:
                device2 = NetworkDevice(d[0], d[2], d[3], d[4])

            devices2_list.append(device2)

        return devices2_list


# Create a function to print the device information (name, IP, username, password),
# and then display the interface information. Don't worry about parsing and printing
# in table format. unless you want to!


def print_device_info(device):

    print('-------------------------------------------------------')
    print('\tDevice Name:\t\t{}'.format(device.name))
    print('\tDevice IP:\t\t{}'.format(device.ip_address))
    print('\tDevice username:\t{}'.format(device.username))
    print('\tDevice password:\t{}'.format(device.password))
    print()
    print('Interfaces')
    print()

    for item in device.interfaces.readlines():
        pprint('{}'.format(item.strip()))

    print('-------------------------------------------------------\n\n')


if __name__ == '__main__':
    devices_list = read_device('device.txt')
    print()
    for device in devices_list:
        device.connect()
        device.get_interfaces()
        print_device_info(device)

