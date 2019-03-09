#Netmiko3.py - simple manipulation of dictionary list

from netmiko import ConnectHandler

cisco_IOSv = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.222",
    "username": "ant",
    "password": "cisco",
}

net_connect = ConnectHandler(**cisco_IOSv)

output = net_connect.send_command("sh ip int br", use_textfsm=True)


#print the length of the list - no of entries
print("Number of interfaces =" , len(output))
print("\n")

print("Interface: "+ output[0].get("intf") + "  IP Adddress:  "+ output[0].get("ipaddr"))

---------------------------------------------------------------------------------
('Number of interfaces =', 4)


Interface: GigabitEthernet0/0  IP Adddress:  192.168.122.222
