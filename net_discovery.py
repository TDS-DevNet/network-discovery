import paramiko
import csv

# create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect to the device
client.connect('device_ip', username='user', password='pass')

# create a list to store the device information
device_info = []

# retrieve CDP neighbor information
cdp_output = client.send_command('show cdp neighbors')
cdp_lines = cdp_output.split('\n')
for line in cdp_lines:
    if 'Eth' in line:
        fields = line.split()
        device_info.append({
            'site': '',  # add the site or location here
            'hostname': fields[0],
            'model': fields[1],
            'mgmt_ip': fields[2],
            'port': fields[-1]
        })

# retrieve device information
version_output = client.send_command('show version')
for line in version_output.split('\n'):
    if 'board ID' in line:
        serial_number = line.split()[-1]
    elif 'uptime is' in line:
        hostname = line.split()[0]
    elif 'System image file is' in line:
        firmware = line.split()[-1]

device_info.append({
    'site': '',  # add the site or location here
    'hostname': hostname,
    'serial_number': serial_number,
    'firmware': firmware
})

# retrieve interface information
ip_output = client.send_command('show ip interface brief')
for line in ip_output.split('\n'):
    if 'MGMT' in line:
        fields = line.split()
        mgmt_ip = fields[1]

# add management IP to the device information
for i in range(len(device_info)):
    if device_info[i]['hostname'] == hostname:
        device_info[i]['mgmt_ip'] = mgmt_ip

# close the SSH connection
client.close()

# write the device information to a CSV file
with open('device_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['site', 'hostname', 'model', 'serial_number', 'mgmt_ip', 'port', 'firmware']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for info in device_info:
        writer.writerow(info)
