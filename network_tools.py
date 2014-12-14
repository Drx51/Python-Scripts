#!/usr/bin/python
# -*- coding: utf8 -*-
#Calculette réseau

import sys

(addrString,cidrString) = sys.argv[1].split('/')

addr = addrString.split('.')
cidr = int(cidrString)
mask = [0,0,0,0]
for i in range(cidr):
	mask[i/8] = mask[i/8] + (1 << (7 - i % 8))
	net = []
	for i in range(4):
		net.append(int(addr[i]) & mask[i])
		broad = list(net)
		brange = 32 - cidr
	for i in range(brange):
		broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

print "Address: " , addrString
print "Netmask: " , ".".join(map(str,mask))
print "Network: " , ".".join(map(str,net))
print "Broadcast " , ".".join(map(str,broad))
