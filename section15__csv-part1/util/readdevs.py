from devclass.basedev import NetworkDevice
from devclass.iosdev import NetworkDeviceIOS
import csv


def read_device(devices_file):
    devices2_list = list()

    with open(devices_file, 'r') as f:
        csv_devices = csv.reader(f)
        device_info = [dev_info for dev_info in csv_devices]

        for d in device_info:
            if d[1] == 'ios':
                device2 = NetworkDeviceIOS(d[0], d[2], d[3], d[4])

            elif device_info[1] == 'ios-xr':

                device2 = NetworkDeviceXR(d[0], d[2], d[3], d[4])

            else:
                device2 = NetworkDevice(d[0], d[2], d[3], d[4])

            devices2_list.append(device2)

        return devices2_list
