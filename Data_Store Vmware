#!/usr/bin/env python

# Complete the following variables for your configuration
#
report="./vm-per-datastore-usage.csv" # name of the report file
vcenterhostlist=['vcenter1.mydomain.com','vcenter2.mydomain.com'] # List of servers to query
vcenteruser="mydomain.com\myuser"
vcenterpwd="mypassword"

from pysphere import *
import sys
import os

# Initialize an empty report file with Header
f=open(report,'w',0)
f.write("vCenterHost;vMname;vm_owner;vm_function;DataStore_Name;storage_committed;storage_uncommitted;perDataStore_Total\n")
f.close

server = VIServer()

for vcenterhost in vcenterhostlist:

  server.connect(vcenterhost,vcenteruser,vcenterpwd)
  if (vcenterhost == 'dc1-vim-vc-01.cpc998.be'):
    owner_field="103"
    function_field="104"
  elif (vcenterhost == 'dc2-vim-vc-01.cpc998.be'):
    owner_field="3"
    function_field="5"
  else:
    owner_field="103"
    function_field="104"

  f=open(report,'a',0)

  vmlist = server.get_registered_vms()
  for vm in vmlist:
    vm_mor = server.get_vm_by_path(vm)
    vm_name = vm_mor.properties.config.name
    try:
      numberOfValues = len(vm_mor.properties.summary.customValue)
      i = 0
      if numberOfValues > 0:
        while (i < numberOfValues):
          currentKey = vm_mor.properties.summary.customValue[i].key
          if (currentKey == int(owner_field)):
            vm_owner = vm_mor.properties.summary.customValue[i].value
          elif (currentKey == int(function_field)):
            vm_function = vm_mor.properties.summary.customValue[i].value
          i = i + 1
    except:
      vm_owner = " "
      vm_function = " "  
    for usage in vm_mor.properties.storage.perDatastoreUsage:
      #print vm_name, usage.datastore.name, usage.committed / 1024 ** 3
      datastore_name = usage.datastore.name
      datastore_committed = str(usage.committed / 1024 ** 3)
      datastore_uncommitted = str(usage.uncommitted / 1024 ** 3)
      datastore_usage_total = (usage.committed / 1024 ** 3) + (usage.uncommitted / 1024 ** 3)
      reportline = vcenterhost + ";" + vm_name + ";" + vm_owner + ";" + vm_function + ";" + datastore_name + ";" + datastore_committed + ";" + datastore_uncommitted  + ";" + str(datastore_usage_total) + "\n"
      f.write(reportline)
  
  f.close
  server.disconnect # end of the for host in vcenterhostlist
