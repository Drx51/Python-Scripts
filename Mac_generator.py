#!/usr/bin/python
#Mac Generator tool for audit or pentest
  
import random
import argparse
import subprocess
import fcntl, socket, struct
import time
  
parser = argparse.ArgumentParser(
add_help=False, formatter_class=argparse.RawDescriptionHelpFormatter, epilog='Examples: %(prog)s -r -i wlan0')
parser.add_argument('-r', action='store_true', help='Set fully random MAC')
parser.add_argument('-v', action='store_true', help='Enable Verbose Mode')
parser.add_argument('-s', action='store_true', help='Print the MAC address and exit')
parser.add_argument('-i', dest='interface', help='Network Interface', required='yes')
parser.add_argument('-h', action='help', help='Print this help message and exit')
  
args = parser.parse_args()
interface = args.interface
randomized = args.r
show = args.s
verbose = args.v
  
  
def ifconfig_up(interface):
     if verbose == True:
            print 'Putting Interface %s Up' % interface
             subprocess.call(["ifconfig", interface, "up"])
       else:
        subprocess.call(["ifconfig", interface, "up"])
  
def ifconfig_down(interface):
    if verbose == True:
            print 'Putting Interface %s Down' % interface
            subprocess.call(["ifconfig", interface, "down"])
    else:
         subprocess.call(["ifconfig", interface, "down"])
  
  
if randomized == True and interface:
            
    def randomMAC():
        mac = [ random.randint(0x00, 0x00),
            random.randint(0x00, 0x2f),
            random.randint(0x00, 0x48),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff) ]
        return ':'.join(map(lambda x: "%02x" % x, mac))
    
    
    newmac = randomMAC()
    ifconfig_down(interface)
    time.sleep(1)
    subprocess.Popen("ifconfig %s hw ether %s" %(interface,newmac), shell=True)
    time.sleep(1)
    ifconfig_up(interface)
    print 'Faked Mac:',newmac
  
    
if show  == True and interface:
    
    def getHwAddr(ifname):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
            return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]
        
    print getHwAddr(interface)
