from devclass import NetworkDevice
from devclass import NetworkDeviceIOS
from pprint import pprint

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

