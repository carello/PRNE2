import re
from pprint import pprint

# PART 1: Count routes per interface
print('\n--- PART 1 ---')

'''
--- DESIRED OUTCOME ---
{'0/0/0/0': 2, '0/0/0/1': 1, '0/0/0/2': 2}
'''

gig_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9]\/[0-9]\/[0-9])')

routes = dict()

with open('ip-routes.txt', 'r') as f:
    for fl in f.readlines():
        match = gig_pattern.search(fl)
        if match:
            intf = match.group(2)
            # this is tricky code below
            routes[intf] = routes[intf]+1 if intf in routes else 1
pprint(routes)

# PART 2: Tabulate OS Types
print('\n--- PART 2 ---')

'''
--- DESIRED OUTCOME ---
{'Cisco IOS': {'count': 2, 'dev': ['d01-is', 'd02-is']},
 'Cisco IOS-XE': {'count': 2, 'dev': ['d07-xe', 'd08-xe']},
 'Cisco IOS-XR': {'count': 2, 'dev': ['d05-xr', 'd06-xr']},
 'Cisco Nexus': {'count': 2, 'dev': ['d03-nx', 'd04-nx']}}
'''

# Create dictionary of dictionaries for os_types with keys 'Cisco IOS', 'Cisco Nexus',
# 'Cisco IOS-XR', 'Cisco IOS-XE' that counts the different os_types for all devices.
# format as follows: { 'Cisco IOS': {'count': 0, 'devs': []}

os_types = {'Cisco IOS':    {'count': 0, 'dev': []},
            'Cisco Nexus':  {'count': 0, 'dev': []},
            'Cisco IOS-XR': {'count': 0, 'dev': []},
            'Cisco IOS-XE': {'count': 0, 'dev': []}}

with open('devices.txt', 'r') as h:
    for hl in h:
        device_info_list = hl.strip().split(',')

        # For every OS type, create a dictionary (not the one above) with two items:
        # a 'count' (key) for the number of devices of this OS type,
        # and a list of device names of the 'devices' (key) of this device type.
        device_info = dict()
        device_info['name'] = device_info_list[0]
        device_info['os-type'] = device_info_list[1]

        # Get the device name an os-type as variables
        name = device_info['name']
        os = device_info['os-type']

        # Depending on the OS type, increment the count of the correct OS type in your dictionary,
        # and add the name of the device to the list of devices.
        if os == 'ios':
            os_types['Cisco IOS']['count'] += 1
            os_types['Cisco IOS']['dev'].append(name)
        elif os == 'nx-os':
            os_types['Cisco Nexus']['count'] += 1
            os_types['Cisco Nexus']['dev'].append(name)
        elif os == 'ios-xr':
            os_types['Cisco IOS-XR']['count'] += 1
            os_types['Cisco IOS-XR']['dev'].append(name)
        elif os == 'ios-xe':
            os_types['Cisco IOS-XE']['count'] += 1
            os_types['Cisco IOS-XE']['dev'].append(name)
        else:
            print('--- OS not found : {}---'.format(os))

pprint(os_types)



# PART 3: Tabulate OSPF Interfaces
print('\n--- PART 3 ---')

'''
--- DESIRED OUTCOME ---
{'0/0/0/0': [{'next_hop': '58.0.0.21', 'prefix': '11.11.1.0/24'},
             {'next_hop': '58.0.0.21', 'prefix': '11.11.3.0/24'}],
 '0/0/0/1': [{'next_hop': '48.0.0.27', 'prefix': '11.11.5.0/24'}],
 '0/0/0/2': [{'next_hop': '49.0.0.30', 'prefix': '11.11.4.0/24'}]}
 '''

intf_routes = dict()

# Create regular expressions to match interfaces and OSPF
OSPF_pattern = re.compile('^O')
intf_pattern = re.compile('(GigabitEthernet)([0-9]\/[0-9]\/[0-9]\/[0-9])')

# Create regular expressions for match prefix and routes
prefix_pattern = re.compile('^O.{4}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2})')
route_pattern = re.compile('via ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')


# Match OSPF route, if true, then match Interface pattern and add to dict. then extract prefix and next_hop
# as a new dictionary and add as a list to original dictionary
with open('ospf-routes.txt', 'r') as r:
    for rl in r:
        # match on OSPF pattern
        matched_ospf = OSPF_pattern.search(rl)
        if matched_ospf:
            matched_intf = intf_pattern.search(rl)

            # Get interface port numbers
            if matched_intf:
                intf = matched_intf.group(2)    # get port numbers from match
                if intf not in intf_routes:     # If not in dict, create LIST it now!
                    intf_routes[intf] = []      # notice value is a LIST!

                # For every route created above, create a new dictionary holding
                # the destination IP address/subnet and the next hop.

                # Extract ip prefix and subnet
                matched_prefix = prefix_pattern.search(rl)
                prefix = matched_prefix.group(1)

                # Extract the route
                matched_route = route_pattern.search(rl)
                next_hop = matched_route.group(1)

                # Create new dictionary and add it to the list
                route = {'prefix': prefix, 'next_hop': next_hop}
                intf_routes[intf].append(route)

pprint(intf_routes)
