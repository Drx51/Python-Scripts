#!/usr/bin/env python

__author__  = "Jean-Philippe (devloop)"
__version__ = "1.0"
__usage__   = """Usage : python dvscan.py host_or_ip [timeout]
Default timeout = 3 seconds
scan is a multithreaded port scanner which scans for well known services
"""
import threading
import socket
import errno
import sys
import string

port_list=[21,22,23,25,42,53,69,79,80,110,111,113,119,135,137,138,139,161,389,443,445,513,554,1080,1433,3306,4899,6000,6667,8080,10000]
opened=[]

class Scan(threading.Thread):

  def __init__(self,ip,port,timeout=3):
    threading.Thread.__init__(self)
    self.port=port
    self.ip=ip
    self.timeout=timeout

  def run(self):
    global code
    self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.s.settimeout(self.timeout)
    code=self.s.connect_ex((ip,self.port))
    if code == 0:
    	self.s.shutdown(socket.SHUT_RDWR)
	self.s.close()
	opened.append(self.port)
	print ">> Port",self.port,"ouvert !"
    else:
      if errno.errorcode[code]=="ECONNREFUSED":
        print "Port",self.port,"ferme !"
      else:
        if errno.errorcode[code]=="EHOSTUNREACH":
	  print "Port",self.port,": Host Unreachable !"
	else:
	  print "Port",self.port,": Timeout !"

  def get_code(self):
    global code
    return code


if __name__ == "__main__":
  print sys.argv[0],__version__
  if len(sys.argv) >= 2:
    ip=sys.argv[1]
    ip2=["","",""]
    timeout=3
    try:
      ip2=socket.gethostbyaddr(ip)
    except socket.gaierror:
      print ip,": Unknown host !!"
      sys.exit()
    except socket.herror:
      pass
    if len(sys.argv) >=3:
      try:
        timeout=string.atoi(sys.argv[2])
      except ValueError:
        timeout=3
    if ip2[0]=="":
      ip2[0]=ip
    print "Launching scan on",ip2[0],ip2[2]
    print "--------------------------------"
    threadlist=[]
    for p in port_list:
      scan=Scan(ip,p,timeout)
      scan.start()
      threadlist.append(scan)
    for scan in threadlist:
      scan.join()
    print "\nPort ouverts :"
    print "--------------"
    opened.sort()
    for p in opened:
      try:
        print p,":",socket.getservbyport(p)
      except socket.error:
        print p
  else:
    print __usage__
