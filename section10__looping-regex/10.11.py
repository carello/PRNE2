
# In this exercise, you will readIP route information from a device.
# You will allow a user to enter IP address prefixes and will display
# route information if the route was learned via OSPF.


import re

with open('ospf-routes.txt', 'r') as f:
    routes_list = [line.strip() for line in f.readlines()]

#for r in routes_list:
#    pprint(r)
print()

while True:
    try:
        ip_ask = input('Enter IP destination to find [CTRL-C to exit]: ')
    except KeyboardInterrupt:
        print('')
        break

    # Set pattern for OSPF routes
    route_pattern = re.compile('^O.{4}([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')

    for r in routes_list:
        route_lookup = route_pattern.search(r)
        if not route_lookup:
            continue

        route_match = route_lookup.group(1)
        if route_match == ip_ask:
            print(route_info)
            print(' ---- Route: {}'.format(route_info[0][5:].strip()))
            print(' ---- Time: {}'.format(route_info[1].strip()))
            print(' ---- Interface: {}'.format(route_info[2].strip()))
            break
    else:
        print('--- No Prefix found ---')

print()




