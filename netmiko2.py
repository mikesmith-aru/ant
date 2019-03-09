# Netmiko2.py - extracts basic data from list of dictionaries

from netmiko import ConnectHandler

cisco_IOSv = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.222",
    "username": "ant",
    "password": "cisco",
}

net_connect = ConnectHandler(**cisco_IOSv)

output = net_connect.send_command("sh ip int br", use_textfsm=True)
print(output)
#
#print the first element of the list
print(output[0])
#
#print the length of the list - no of entries
print("Number of interfaces =" , len(output))

print(output[0].get("intf"))

----------------------------------------------------------------------------------
[{'status': 'up', 'intf': 'GigabitEthernet0/0', 'ipaddr': '192.168.122.222', 'proto': 'up'}, {'status': 'administratively down', 'intf': 'GigabitEthernet0/1', 'ipaddr': 'unassigned', 'proto': 'down'}, {'status': 'administratively down', 'intf': 'GigabitEthernet0/2', 'ipaddr': 'unassigned', 'proto': 'down'}, {'status': 'administratively down', 'intf': 'GigabitEthernet0/3', 'ipaddr': 'unassigned', 'proto': 'down'}]
{'status': 'up', 'intf': 'GigabitEthernet0/0', 'ipaddr': '192.168.122.222', 'proto': 'up'}
('Number of interfaces =', 4)
GigabitEthernet0/0

