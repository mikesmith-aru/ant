#Basic Python script using PySNMP to get SNMP OIDs

from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

system_up_time_oid = "1.3.6.1.2.1.1.3.0"
cisco_contact_info_oid = "1.3.6.1.4.1.9.2.1.61.0"

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData("secret"),
    cmdgen.UdpTransportTarget(("192.168.122.222", 161)),
    system_up_time_oid,
    cisco_contact_info_oid
)

#check for errors and print results

if errorIndication:
   print(errorIndication)
else:
   if errorStatus:
      print("%s at %s" % (
         errorStatus.prettyPrint(),
         errorIndex and varBinds[int (errorIndex)-1] or "?"
         )
      )
   else:
       for name, val in varBinds:
         print("%s = %s" % (name.prettyPrint(), str(val)))
