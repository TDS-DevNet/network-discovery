# Gathering Device Information Using SSH and Cisco IOS Commands

To gather the desired information about the devices in your network using SSH and Cisco IOS commands, you will need to do the following:

1. Connect to the core devices using SSH: You can use a library such as `paramiko` in Python to establish an SSH connection to the core devices. Once connected, you can run Cisco IOS commands on the devices using the `send_command()` function.

2. Retrieve CDP neighbor information: You can use the `show cdp neighbors` command to retrieve information about the devices that are directly connected to the current device. This command will show you the hostname, model number, and IP address of each neighbor device, as well as the port that the devices are connected on.

3. Retrieve device information: You can use the following commands to retrieve the rest of the information you are interested in:

- `show version`: This command will show you the device's hostname, model number, serial number, and software version.

- `show ip interface brief`: This command will show you the IP addresses of the device's interfaces. You can use the management interface's IP address as the management IP address of the device.

- `show boot`: This command will show you the firmware that the device is currently running.

4. Store the information: You can store the information you retrieve in a .csv file or a database for later analysis. You can use a library such as Python's `csv` module to create and write to the .csv file.

# Setting up a Python Environment

To set up a Python environment to run the code:

1. Install Python and pip: If you do not already have Python installed on your system, you will need to install it. You can download the latest version of Python from the [Python website](https://www.python.org/downloads/).

<details>
<summary>Install pip and create python virtual environment</summary>

## Downloading pip and Creating a Python Virtual Environment

To download `pip` and create a Python virtual environment, you will need to do the following:

1. Install Python: If you do not already have Python installed on your system, you will need to install it. You can download the latest version of Python from the [Python website](https://www.python.org/downloads/).

2. Install `pip`: `pip` is included with Python versions 3.4 and higher. If you are using an older version of Python, you will need to install `pip` separately. To install `pip`, you can use the following command:

`python -m ensurepip --default-pip`

This will install `pip` and any other required dependencies.

3. Create a virtual environment: A virtual environment is a separate Python environment that allows you to install packages and libraries in isolation from the global Python environment. To create a virtual environment, you can use the following command:

`python -m venv env`


This will create a virtual environment named `env`. You can replace `env` with the desired name for your virtual environment.

4. Activate the virtual environment: To activate the virtual environment, you will need to use the `activate` script that is located in the `env/bin` directory.

On Windows, you can use the following command: `env\Scripts\activate.bat`


On Linux or macOS, you can use the following command:

`source env/bin/activate`

Once the virtual environment is activated, you will see the name of the virtual environment in the terminal or command prompt, like this:

Windows - `(env) C:\path\to\project\directory>`
Linux/Mac - `(env) user@host:~$ `


</details>


2. Install the required libraries: The script requires the `paramiko` and `csv` libraries. You can install these libraries using `pip`, the Python package manager. Open a terminal or command prompt and enter the following command:

`pip install paramiko csv`


3. Clone the script: If you want to run the script directly from GitHub, you can clone the repository containing the script. To do this, enter the following command in a terminal or command prompt:

`git clone https://github.com/TDS-DevNet/network-discovery.git`

5. Make necessary changes to fit your network

6. Run the script with python

`python3 net_discovery.py`


