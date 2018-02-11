from pprint import pprint
import binascii

#==========================================================================
def print_device_info(device):

    print('-------------------------------------------------------')
    print('\tDevice Name:\t\t{}'.format(device.name))
    print('\tDevice IP:\t\t{}'.format(device.ip_address))
    print('\tDevice username:\t{}'.format(device.username))
    print('\tDevice password:\t{}'.format(device.password))
    print()
    print('Interfaces')
    print()

    print(binascii.hexlify(device.sshkey))

    print('-------------------------------------------------------\n\n')
