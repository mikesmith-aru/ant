#Fetch SNMP variable

#varBinds is a set of tuples containing the values of the response
#mpModel defines the SNMP version 0 = SNMPv1; 1 = SNMPv2c

from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
     getCmd(SnmpEngine(),
            CommunityData("secret", mpModel=0),
            UdpTransportTarget(("192.168.122.222", 161)),
            ContextData(),
            ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr",0)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print("%s at %s" % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex)-1][0] or "?"))
else:
    for varBind in varBinds:
        print("=".join([x.prettyPrint() for x in varBind]))
