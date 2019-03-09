# Program to print the status of each device interface
#netmiko4.py

from netmiko import ConnectHandler

cisco_IOSv = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.222",
    "username": "ant",
    "password": "cisco",
}

net_connect = ConnectHandler(**cisco_IOSv)

output = net_connect.send_command("sh ip int br", use_textfsm=True)
# print(output)

#print header
print("-" * 40 + "\n")
print("Interface             Status" + "\n")

for item in output:
  print(item.get("intf") + "    " +item.get("status"))

print("\n" * 3)
root@UbuntuDockerGuest-1:~# python netmiko4.py
----------------------------------------

Interface             Status

GigabitEthernet0/0    up
GigabitEthernet0/1    administratively down
GigabitEthernet0/2    administratively down
GigabitEthernet0/3    administratively down

