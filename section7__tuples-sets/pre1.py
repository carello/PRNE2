dev_list = [i for i in range(3)]

dev30 = {'name':'ios','ip':'10.1.1.30','user':'cisco'}
dev31 = {'name':'ios','ip':'10.1.1.31','user':'cisco'}
dev32 = {'name':'ios','ip':'10.1.1.32','user':'cisco'}

dev40 = {'name':'xr','ip':'10.1.1.30','user':'cisco'}
dev41 = {'name':'xr','ip':'10.1.1.31','user':'cisco'}
dev42 = {'name':'xr','ip':'10.1.1.32','user':'cisco'}

# List of dictionaries
print('\nList of Dictionaries')
dev_list[0] = dev30
dev_list.append(dev31)
print(dev_list)

# Dictionary of Dictionaries
print('\nDictionary of Dictionaries')
devices = dict()
devices['chet'] = dev30
devices['pasta'] = dev31
devices['ray'] = dev32
print(devices)

# Dictionary of List of Dictionaries
print('\nDictionary of List of Dictionaries')
ios_devices = list()
ios_devices.append(dev30)
ios_devices.append(dev31)
ios_devices.append(dev32)
xr_devices = list()
xr_devices.append(dev40)
xr_devices.append(dev41)
xr_devices.append(dev42)

all_devices = dict()
all_devices['ios'] = ios_devices
all_devices['xr'] = xr_devices
print(all_devices)
