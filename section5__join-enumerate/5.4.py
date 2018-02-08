# read a file line by line only
# print out in a table like format
# make a string from the data and write to new file
# read in the new file and print in a table like format

# Read file line by line
with open('dev-01-info', 'r') as f:
    name = f.readline().strip()
    ip = f.readline().strip()
    os = f.readline().strip()
    user = f.readline().strip()
    pw = f.readline().strip()

# Print out in table format
print('{0:10} {1:15} {2:10} {3:15} {4:15}'.format('Device', 'IP Address', 'OS Type', 'User', 'Password'))
print('{0:10} {1:15} {2:10} {3:15} {4:15}'.format(name, ip, os, user, pw))

# Create string from data
my_str = ','.join([name, ip, os, user, pw])

# Write string to new file
with open('device_info.txt', 'w') as g:
    g.write(my_str)

# Read in the new file in table format
print('-' * 26)
prn_template = '{:<12}: \t{:<20}'
keys = ['Device', 'IP Address', 'OS Type', 'User', 'Password']
print('--- Device data ---')

with open('device_info.txt', 'r') as infile:
    data = infile.readline().strip().split(',')
    for item, (k, d) in enumerate(zip(keys, data)):
        print(prn_template.format(k, d))

