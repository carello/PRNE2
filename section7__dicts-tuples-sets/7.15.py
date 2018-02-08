
from pprint import pprint
from collections import namedtuple

# PART 1: Create a tuple
print('\n--- PART 1: Tuple ---')
with open('device.txt', 'r') as f:
    file_line = f.readline().strip()
    my_tuple = tuple(file_line.split(','))
pprint(my_tuple)


# PART 2: Create a 'List of Tuples' to Hold Device Information
# About Multiple Devices
print('\n--- PART 2: List of Tuples ---')
device_list2 = list()
with open('devices-multi.txt', 'r') as g:
    for gl in g:
        my_tuple2 = tuple(gl.strip().split(','))
        device_list2.append(my_tuple2)
pprint(device_list2)


# PART 3: Create a Dictionary of Named Tuples Which Hold Device Information
print('\n--- PART 3: Dict of named tuples ---')
Dev_info3 = namedtuple('Dev_info3', ['name', 'os', 'ip', 'user', 'pw'])
devices3 = dict()

with open('devices-multi.txt', 'r') as h:
    for hl in h:
        device_info3 = Dev_info3(*(hl.strip().split(',')))
        devices3[device_info3.name] = device_info3
pprint(devices3)


# PART 4: Create a Set of All the OS Types Present for the List of Devices
# Read from a File
print('\n--- PART 4: Set of OS Types ---')
Dev_info4 = namedtuple('Dev_info4', ['name', 'os', 'ip', 'user', 'pw'])
os_types = set()
with open('devices-multi.txt', 'r') as j:
    for jl in j:
        device_info4 = Dev_info4(*(jl.strip().split(',')))

        if device_info4.os not in os_types:
            os_types.add(device_info4.os)

pprint(os_types)
print(type(os_types))



