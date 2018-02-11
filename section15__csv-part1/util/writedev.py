import csv


def prn_output(device):
    prn_lst = list()
    for item in device.interfaces.readlines():
        prn_lst.append(item)
    return prn_lst


def write_devices_info(devices_file, devices_list):
    print('---- Printing CSV output ------------------------------')

    # Create the list of lists with devices and device info
    devices_out_list = []  # create list for CSV output

    for device in devices_list:
        dev_info = [device.name, device.ip_address, prn_output(device)]
        devices_out_list.append(dev_info)


    # Use CSV library to output our list of lists to a CSV file
    with open(devices_file, 'w') as file:
        csv_out = csv.writer(file)
        csv_out.writerows(devices_out_list)


