from devclass.basedev import NetworkDevice
from devclass.iosdev import NetworkDeviceIOS
import json
from pprint import pprint


def read_device(devices_file):
    devices2_list = list()

    with open(devices_file, 'r') as json_file:
        json_device_data = json_file.read()
        devices_info_list = json.loads(json_device_data)

        for d in devices_info_list:
            if d['os'] == 'ios':
                device2 = NetworkDeviceIOS(d['name'], d['ip'], d['user'], d['password'])

            elif d['os'] == 'ios-xr':

                device2 = NetworkDeviceXR(d['name'], d['ip'], d['user'], d['password'])

            else:
                device2 = NetworkDevice(d['name'], d['ip'], d['user'], d['password'])

            # After reading the file, pass the binary data object to the device object.
            # The device object will need to implement a method such as 'set_sshkey'
            # which is passed the binary data object you have just read.
            key_file_path = 'sshkeys/'+d['key']
            key_file = open(key_file_path, 'rb')
            key_data = key_file.read()
            device2.set_sshkey(key_data)

            devices2_list.append(device2)

        return devices2_list
