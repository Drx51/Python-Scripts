#!/usr/bin/env python

# Complete the following variables of your configuration

vcenterhost="vcenter1.mydomain.com"
vcenteruser="mydomain.com\myuser"
vcenterpwd="mypassword"

######################################################
from pysphere import *
import pprint
server = VIServer()
server.connect(vcenterhost,vcenteruser,vcenterpwd)

vm = server.get_vm_by_path('[N6060_SAS_JABLUX_VM01] S998JPLNX236PRD-Dhcp/S998JPLNX236PRD-Dhcp.vmx')
print '='*70
prop = vm.get_properties()

print prop
print type(prop)
server.disconnect
