import paramiko

def connect(host, login, pw):
    print('--- Attempting connection to {}'.format(host))
    ssh_client = paramiko.SSHClient()

    # Must set missing host key policy since we don't have the SSH key stored in the 'known_hosts' file
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Make the connection to our host.
    try:
        ssh_client.connect(hostname=host, username=login, password=pw)
        # Execute some commands
    except Exception as e:
        sys.stderr.write("\n--- SSH connection error: {} ---".format(e))

    return ssh_client


def do_command(connection, cmd):
    stdin, stdout, stderr = connection.exec_command(cmd)
    data = [line.strip('\n') for line in stdout.readlines()]
    return data


def prn_output(h, l, data):
    print('{0:10} {1:15}'.format(h, l))
    print()
    for d in data:
        print(d)


if __name__== '__main__':
    user = 'chet'
    password = 'letmein'
    host = '10.91.86.244'
    login = user
    pw = password
    cisco_command = "show ip interface brief"

    connection = connect(host, login, pw)
    device_info = do_command(connection, cisco_command)
    prn_output(host, login, device_info)





