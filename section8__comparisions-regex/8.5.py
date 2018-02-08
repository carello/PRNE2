import re
from pprint import pprint

# PART 1: Find bad versions
print('\n--- PART 1 ---')
current_version = 'Version 5.3.1'

with open('devices.txt', 'r') as f:
    for fl in f:
        device_info_list = fl.strip().split(',')

        device_info = dict()
        device_info['name'] = device_info_list[0]
        device_info['OS-type'] = device_info_list[1]
        device_info['IP-address'] = device_info_list[2]
        device_info['version'] = device_info_list[3]
        device_info['username'] = device_info_list[4]
        device_info['password'] = device_info_list[5]

        if device_info['version'] != current_version:
            print('Device: {}\t{}'.format(device_info['name'], device_info['version']))


# PART 1B Same as PART 1 but with list comp
print('\n--- PART 1B ---')
with open('devices.txt', 'r') as ff:
    ff_file = [line.strip().split(',') for line in ff.readlines()]

for item in ff_file:
    device_info = dict()
    device_info['name'] = device_info_list[0]
    device_info['OS-type'] = device_info_list[1]
    device_info['IP-address'] = device_info_list[2]
    device_info['version'] = device_info_list[3]
    device_info['username'] = device_info_list[4]
    device_info['password'] = device_info_list[5]

    if device_info['version'] != current_version:
        print('Device: {}\t{}'.format(device_info['name'], device_info['version']))



# PART 2: Extract IP address using regex
print('\n--- PART 2 ---')

ip_pattern = re.compile('Mgmt:([0-9]*\.[0-9]*\.[0-9]*\.[0-9])')

with open('devices.txt', 'r') as g:
    for gl in g:
        device_info_list2 = gl.strip().split(',')

        device_info2 = dict()
        device_info2['name'] = device_info_list2[0]
        mgmt_addr = ip_pattern.search(gl)

        print('{0:8}: \t{1:20}'.format(device_info2['name'], mgmt_addr.group(1)))


# PART 3: same as Part 2 but with list comp
print('\n--- PART 3 ---')

with open('devices.txt') as h:
    h_file = [line.strip().split(',') for line in h.readlines()]

for item in h_file:
    device_info3 = dict()
    device_info3['name'] = item[0]
    mgmt_addr3 = ip_pattern.search(item[2])

    print('{0:10} {1:10}'.format(device_info3['name'], mgmt_addr3.group(1)))






