from pprint import pprint

# PART 1
device_info_list = list()

def prn_dev():
    print('{0:10} {1:10} {2:20} {3:20}'.format('Device', 'OS Type', 'IP Address', 'Version'))
    for d in device_info_list:
        print('{0:10} {1:10} {2:20} {3:20}'.format(*d))


def dev_read():
    with open('devices.txt', 'r') as f:
        device_info = [line.strip().split(',') for line in f.readlines()]
    return device_info


#if __name__ == '__main__':
#    device_info_list = dev_read()
#    prn_dev()



# PART 2
print('\n--- PART 2 ---')

def dev_read2(filename):
    with open(filename, 'r') as ff:
        device_info2 = [line.strip().split(',') for line in ff.readlines()]
    return device_info2


def prn_dev2(dev):
    print('{0:10} {1:10} {2:20} {3:20}'.format('Device', 'OS Type', 'IP Address', 'Version'))
    for d in dev:
        print('{0:10} {1:10} {2:20} {3:20}'.format(*d))


if __name__ == '__main__':
    devices_sel = input('enter file name: ')
    device_info_list2 = dev_read2(devices_sel)
    prn_dev2(device_info_list2)

