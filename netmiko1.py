# Basic netmiko program to print the routing table

from netmiko import ConnectHandler

cisco_IOSv = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.222",
    "username": "ant",
    "password": "cisco",
}

net_connect = ConnectHandler(**cisco_IOSv)

output = net_connect.send_command("sh ip int br")
print(output)

------------------------------------------------------------------------------   

Interface                  IP-Address      OK? Method Status                Prot       ocol
GigabitEthernet0/0         192.168.122.222 YES NVRAM  up                    up         
GigabitEthernet0/1         unassigned      YES NVRAM  administratively down down       
GigabitEthernet0/2         unassigned      YES NVRAM  administratively down down       
GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down