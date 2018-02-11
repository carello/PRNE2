

class NetworkDevice(object):
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.os_type = None
        self.sshkey = None


    def connect(self):
        self.session = None


    def get_interfaces(self):
        self.interfaces = "Base device, cannot get interfaces"

    def set_sshkey(self, sshkey):
        self.sshkey = sshkey

