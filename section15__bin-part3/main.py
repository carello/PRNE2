from util.readdevs import read_device
from util.printdev import print_device_info
from util.writedev import write_devices_info

if __name__ == '__main__':
    devices_list = read_device('devices-bin.json')
    print()
    for device in devices_list:
        device.connect()
        device.get_interfaces()

        # Seem ot have a threading problem, only can do one of these lines at a time
        write_devices_info('json-devices-out', devices_list)
        print_device_info(device)



