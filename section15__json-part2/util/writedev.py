import json


def write_devices_info(devices_file, devices_list):
    print('---- Printing JSON output ------------------------------')

    # Create the list of lists with devices and device info
    devices_out_list = []  # create list for CSV output

    for device in devices_list:
        dev_info = {'name': device.name, 'ip': device.ip_address, 'os': device.os_type, 'user': device.username, 'password': device.password}
        devices_out_list.append(dev_info)

    json_device_data = json.dumps(devices_out_list)

    with open(devices_file, 'w') as json_file:
        json_file.write(json_device_data)




