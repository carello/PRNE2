from pprint import pprint


class NetworkDevice(object):
    def device(self, name, os, ip, user='cisco', pw='cisco'):
        self.name = name
        self.os_type = os
        self.ip_address = ip
        self.username = user
        self.password = pw


# Define a function to print a table of device information (name, OS-type,IP, username, password)
# for every device. Pass in a list of devices, where each device is an object of type NetworkDevice.
def prn(device_list):
    for d in device_list:
        print('{0:10} {1:15} {2:15} {3:10} {4:10}'.format(d.name, d.os_type, d.ip_address, d.username, d.password))
    print()


dev1 = NetworkDevice()
dev1.device('dev1', 'IOS', '9.9.9.9')
dev2 = NetworkDevice()
dev2.device('dev2', 'IOS-XR', '8.88.8.8', 'chet', 'connie')

prn([dev1, dev2])

# PART 2:
# define a network device class, with an initialization method for setting
# attributes for each created object.

# Define a class called NetworkDevice2. Define an initialization method (called __init__)
# within the class that takes device information as parameters (device name, OS-type,
# IP address, username, and password
print('\n--- PART 2 ---')

class NetworkDevice2(object):
    def __init__(self, name, os, ip, user, pw):
        self.name = name
        self.os_type = os
        self.ip_address = ip
        self.username = user
        self.password = pw

def dev(device_file):
    devices = list()
    with open(device_file, 'r') as f:
        f_file = [line.strip().split(',') for line in f.readlines()]
        for fl in f_file:
            device = NetworkDevice2(fl[0], fl[1], fl[2], fl[3], fl[4])
            devices.append(device)
    return devices

def prn_dev(stuff):
    for d in stuff:
        print('{0:10} {1:15} {2:15} {3:10} {4:10}'.format(d.name, d.os_type, d.ip_address, d.username, d.password))
    print()

my_devices = dev('real-devices.txt')
prn_dev(my_devices)

