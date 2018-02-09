from pprint import pprint
import re
import sys

# PART 1
prn_template = '{0:10} {1:10} {2:20} {3:20}'

print('\n--- PART 1 ---')

# Read device information from the file and store in a list.
with open('devices.txt', 'r') as f:
    devices_list = [line.strip().split(',') for line in f.readlines()]

pprint(devices_list)
print('\n')

# PART 2
# Print the device information in a table. If an IP address is a duplicate
# of one seen before, print a message indicating it is a duplicate.
print('--- PART 2 ---')
print(prn_template.format('Name', 'OS_Type', 'IP Address', 'Software'))
print('-' * 90)

ip_addresses = set()

for item in devices_list:
    print(prn_template.format(*item), end='')
    if item[2] in ip_addresses:
        print('\t* Duplicate IP Address *')
        continue
    ip_addresses.add(item[2])
    print('')


# PART 3
# allows a user to search for device information by entering the IP address.
# If the IP address is found, the application will display the device information.
# The application will iterate until the user enters Ctrl-C.
print('\n--- PART 3 ---')
ip_pattern = re.compile('Mgmt:([0-9]*\.[0-9]*\.[0-9]*\.[0-9])')

with open('devices.txt') as h:
    devices_list3 = [line.strip().split(',') for line in h.readlines()]

while True:
    try:
        ip_address_sel = input('Enter device IP Address to find [enter Ctrl-C to exit]: ')
    except KeyboardInterrupt:
        print()
        break

    for item in devices_list3:
        ip_find = ip_pattern.search(item[2])
        ip_match = ip_find.group(1)
        if ip_match == ip_address_sel:
            print('{0:10} {1:10} {2:20} {3}'.format(item[0], item[1], item[2], item[3]))
            sys.exit(0)
        else:
            continue

    if ip_address_sel == 'exit':
        break
    else:
        print("--- Given IP address not found ---\n")

'''
# PART 3B : Alternate approach
print("\n--- SELECT BY IP\n")
devices_list3b = list()
print('TEST')
with open('devices.txt', 'r') as gfile:
    for gl in gfile:
        device_info3b = gl.split(',')
        devices_list3b.append(device_info3b)

while True:
    try:
        ip_address3 = input('enter IP Address, [enter "quit" to exit ]: ')
    except KeyboardInterrupt:
        print('')
        break

    for item, index in enumerate(devices_list3b):
        if index[2][5:] == ip_address3:
            print('{0:10} {1:10} {2:20} {3}'.format(index[0], index[1], index[2], index[3]))
            sys.exit(0)
        else:
            continue

    if ip_address3 == 'exit':
        break
    else:
        print("--- Given IP address not found ---\n")
'''

