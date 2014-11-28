#!/usr/bin/env python

# Complete the following variables
#
report="./vm-per-vmguest-usage.csv" # name of the report file
vcenterhostlist=['vcenter1.mydomain.com','vcenter2.mydomain.com'] # List of servers to query
vcenteruser="mydomain.com\myuser"
vcenterpwd="mypassword"


######################################################

from pysphere import *
import sys
import os

# Initialize an empty report file with Header
f=open(report,'w',0)
f.write("vCenterHost;vMname;vm_owner;vm_function;vm_DiskPath;vm_DiskCapacity;vm_DiskFreeSpace\n")
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
      
    try:
      for disk in vm_mor.properties.guest.disk:
	disk_path = disk.diskPath
	disk_capacity = str(float(disk.capacity) / 1024 **3)
	disk_freespace = str(float(disk.freeSpace) / 1024 ** 3)
	reportline = vcenterhost + ";" + vm_name + ";" + vm_owner + ";" + vm_function + ";" + disk_path + ";" + disk_capacity + ";" + disk_freespace + "\n"
	f.write(reportline)
    except:
      disk_path, disk_capacity, disk_freespace = 'NA','NA','NA'
      reportline = vcenterhost + ";" + vm_name + ";" + vm_owner + ";" + vm_function + ";" + disk_path + ";" + disk_capacity + ";" + disk_freespace + "\n"
      f.write(reportline)
      
  f.close
  server.disconnect # end of the for host in vcenterhostlist
