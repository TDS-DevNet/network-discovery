# network-discovery

# Gathering Device Information Using SSH and Cisco IOS Commands

To gather the desired information about the devices in your network using SSH and Cisco IOS commands, you will need to do the following:

1. Connect to the core devices using SSH: You can use a library such as `paramiko` in Python to establish an SSH connection to the core devices. Once connected, you can run Cisco IOS commands on the devices using the `send_command()` function.

2. Retrieve CDP neighbor information: You can use the `show cdp neighbors` command to retrieve information about the devices that are directly connected to the current device. This command will show you the hostname, model number, and IP address of each neighbor device, as well as the port that the devices are connected on.

3. Retrieve device information: You can use the following commands to retrieve the rest of the information you are interested in:

- `show version`: This command will show you the device's hostname, model number, serial number, and software version.

- `show ip interface brief`: This command will show you the IP addresses of the device's interfaces. You can use the management interface's IP address as the management IP address of the device.

- `show boot`: This command will show you the firmware that the device is currently running.

4. Store the information: You can store the information you retrieve in a .csv file or a database for later analysis. You can use a library such as Python's `csv` module to create and write to the .csv file.
