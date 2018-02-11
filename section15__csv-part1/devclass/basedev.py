

class NetworkDevice(object):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.interfaces = ''

    def connect(self):
        self.session = None


    def get_interfaces(self):
        self.interfaces = "Base device, cannot get interfaces"

