# Create a Python application that reads in the device information from the file,
# and puts the items from the file into a Python list

# PART 1: read file and put into a list
print('\n--- PART 1 --- ')
from pprint import pprint
with open('device.txt', 'r') as f:
    fx = [line for line in f.readline().strip().split(',')]
    pprint(fx)


# PART 2: Create a dictionary to hold device information
print('\n--- PART 2 ---')
keys = ['Device', 'OS_Type', 'IP Address', 'User', 'Password']

my_dict = dict()
for item, (k,d) in enumerate(zip(keys, fx)):
    my_dict[k] = d

pprint(my_dict)
print()
# Alternate method
old_dict = dict()
old_dict['name'] = fx[0]
old_dict['os_type'] = fx[1]
old_dict['ip'] = fx[2]
old_dict['user'] = fx[3]
old_dict['pw'] = fx[4]
# pprint(old_dict)


# PART 3: Create a list of dictionaries to hold device information about multiple devices
print('\n--- PART 3 ---')
with open('devices-multi.txt', 'r') as g:
    gx = [line.strip().split(',') for line in g.readlines()]
# pprint(gx)

# Alternate method
device_info_list = list()
with open('devices-multi.txt', 'r') as h:
    for line in h.readlines():
        device_info_list.append(line.strip().split(','))

# pprint(device_info_list)

# However, assignment says put each list into a dict

devices = list()
with open('devices-multi.txt', 'r') as f_file:
    for line in f_file.readlines():
        dev_info_list3 = line.strip().split(',')

        dev_info_dict3 = dict() # we need to reset this dict on every re-iteration!

        # For each device, take the device information and put it into a dictionary.
        dev_info_dict3['name'] = dev_info_list3[0]
        dev_info_dict3['os-type'] = dev_info_list3[1]
        dev_info_dict3['ip'] = dev_info_list3[2]
        dev_info_dict3['user'] = dev_info_list3[3]
        dev_info_dict3['pw'] = dev_info_list3[4]

    # For each device, take the device information dictionary
    # you have created and put the dictionary into the device list.
        devices.append(dev_info_dict3)

pprint(devices)


# PART 4: Create a Dictionary of Dictionaries to Hold Device Information About Multiple Devices.
print('\n--- PART 4 ---')

device4 = dict()
with open('devices-multi.txt', 'r') as h_file:
    for line in h_file.readlines():
        dev_info_list4 = line.strip().split(',')

        dev_info_dict4 = dict() # we need to reset this dict on every re-iteration!

        # For each device, take the device information and put it into a dictionary.
        dev_info_dict4['name'] = dev_info_list4[0]
        dev_info_dict4['os-type'] = dev_info_list4[1]
        dev_info_dict4['ip'] = dev_info_list4[2]
        dev_info_dict4['user'] = dev_info_list4[3]
        dev_info_dict4['pw'] = dev_info_list4[4]

        device4[dev_info_dict4['name']] = dev_info_dict4

pprint(device4)


# PART 5: Create a Dictionary of Lists of Dictionaries to Hold Device Information About Multiple Devices,
# Based on the OS Type for Each Device.
print('\n--- PART 5: ---')
devices5 = dict()
# create dictionary keys with empty lists for the values.
devices5['ios'] = []
devices5['nx-os'] = []
devices5['ios-xr'] = []

with open('devices-multi.txt', 'r') as j_file:
    for line in j_file.readlines():
        dev_info_list5 = line.strip().split(',')

        dev_info_dict5 = dict()

        dev_info_dict5['name'] = dev_info_list5[0]
        dev_info_dict5['os-type'] = dev_info_list5[1]
        dev_info_dict5['ip'] = dev_info_list5[2]
        dev_info_dict5['user'] = dev_info_list5[3]
        dev_info_dict5['pw'] = dev_info_list5[4]

        # Magic happens here. 
        devices5[dev_info_dict5['os-type']].append(dev_info_dict5)

pprint(devices5)






