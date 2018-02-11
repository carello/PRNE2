
# Define a base class for a generic networking device
# and sub-classes for IOS and IOS-XR types of network devices.
# Specifically, you will read the list of devices from a file
# and will create specific types of device objects depending
# on the OS-type of the device.


# Part 1: Define Base and Child Classes
#
# Define a base class for a generic network device, with an initialization
# function to set device name, IP, username, and password. Because the
# device type is unknown for a generic device, set os_type to 'unknown'.
# set user and password to defaults cisco/cisco

print('\n--- Part 1 ---')
print()


class NetworkDevice(object):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.os_type = 'unknown'

# Define two child classes which derive from the base NetworkDevice class.
# One class will be for IOS devices, the other will be for IOS-XR devices.
# Each specific device class will have an initialization function which takes as
# input the device name, IP, username, and password.
# It will set its os_type to the appropriate value.

class NetworkDeviceIOS(NetworkDevice):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)
        self.os_type = 'ios'


class NetworkDeviceXR(NetworkDevice):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice.__init__(self, name, ip, user, pw)
        self.os_type = 'ios-xr'

# Create a function which reads the devices file, creates the device objects,
# and adds them to the list. Your function will create different device objects
# depending on whether the os-type of the device that is read from the file is an IOS device,
# an IOS-XR device, or neither. If neither, your function will ignore the device and continue
# reading the file. Your function should return a list of your created devices objects;
# note that some will be IOS objects, some will be IOS-XR objects.

def read_device_file(dev_file):
    devices_list = list()
    with open(dev_file, 'r') as f_file:
        device_info = [line.strip().split(',') for line in f_file.readlines()]

    for d in device_info:
        if d[1] == 'ios':
            device = NetworkDeviceIOS(d[0], d[2], d[4], d[5])
        elif d[1] == 'ios-xr':
            device = NetworkDeviceXR(d[0], d[2], d[4], d[5])
        else:
            continue

        devices_list.append(device)
    return devices_list

def prn_devices(dev_list):
    print('{0:10} {1:10} {2:20} {3:10} {4:10}'.format('Device', 'OS Type', 'IP Address', 'User', 'Password'))
    for d in dev_list:
        print('{0:10} {1:10} {2:20} {3:10} {4:10}'.format(d.name, d.os_type, d.ip_address, d.username, d.password))

'''
if __name__ == '__main__':
    device_output = read_device_file('devices.txt')
    prn_devices(device_output)
'''


# PART 2: Define Classes and Overriding Methods
# define a base class for a generic networking device and sub-classes for IOS and IOS-XR devices.
# You will also override a method to have specific implementations of the method for each child class.
print('\n--- PART 2 ---')
print()

# Define a base class for a generic network device, with an initialization function to set device name,
# IP, username, and password. Note: for this exercise you will not be storing os_type.
# You will be creating methods which return the OS type specifically for the base or child classes.
# There will be a method for the base class called get_type which returns base.


class NetworkDevice2(object):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def get_type(self):
        return 'base'


# Define two child classes which derive from the base NetworkDevice class.
# One class will be for IOS devices, the other will be for IOS-XR devices.
# Each specific device class will have an initialization function which takes as
# input the device name, IP, username, and password.
#
# Create methods for each child class called get_type. For the IOS class,
# this method will return 'IOS', for the XR class, this method will return 'IOS-XR'
#
# In your initialization method, rather than setting your attributes directly,
# you will call into the initialization method for your base class to set the
# attributes for name, IP, username, and password.

class NetworkDeviceIOS2(NetworkDevice2):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice2.__init__(self, name, ip, user, pw)

    def get_type(self):
        return 'IOS'


class NetworkDeviceXR2(NetworkDevice2):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        NetworkDevice2.__init__(self, name, ip, user, pw)

    def get_type(self):
        return 'IOS-XR'


# Create a function which takes as input the name of the devices file and creates device objects
# appropriate to the device os-type. Do not skip any devices:
# if it is an IOS-XR device, create an XR object; if it is an IOS device, create an IOS object; if it is neither,
# then create the generic, base type of device. Your function will return a list of your created devices objects;
# some will be IOS objects, some will be XR objects, and some will be base objects.

def read_device_file2(dev_file2):
    devices_list2 = list()
    with open(dev_file2, 'r') as f_file:
        device_info2 = [line.strip().split(',') for line in f_file.readlines()]

    for d in device_info2:
        if d[1] == 'ios':
            device2 = NetworkDeviceIOS2(d[0], d[2], d[4], d[5])
        elif d[1] == 'ios-xr':
            device2 = NetworkDeviceXR2(d[0], d[2], d[4], d[5])
        else:
            device2 = NetworkDevice2(d[0],d[2], d[4], d[5])

        devices_list2.append(device2)
    return devices_list2

def prn_devices2(dev_list2):
    print('{0:10} {1:10} {2:20} {3:10} {4:10}'.format('Device', 'OS Type', 'IP Address', 'User', 'Password'))
    for d in dev_list2:
        print('{0:10} {1:10} {2:20} {3:10} {4:10}'.format(d.name, d.get_type(), d.ip_address, d.username, d.password))


if __name__ == '__main__':
    device_output2 = read_device_file2('devices.txt')
    prn_devices2(device_output2)

