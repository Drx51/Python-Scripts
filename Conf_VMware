#!/usr/bin/env python

#Edite conf for your configuration

vcenterhost="vcenter1.mydomain.com"
vcenteruser="mydomain.com\myuser"
vcenterpwd="mypassword"

######################################################
from pysphere import *
import pprint
server = VIServer()
server.connect(vcenterhost,vcenteruser,vcenterpwd)
vmlist = server.get_registered_vms()
for item in vmlist:
  vm = server.get_vm_by_path(item)
  print "name:", vm.get_property('name'), "path:", vm.get_property('path')

print "-"*70
print vmlist

server.disconnect
