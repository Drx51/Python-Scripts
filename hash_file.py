#!/usr/bin/env python
# md5checker.py
import os,hashlib,time,sys

def md5_file(file, block_size=2**20):
    try:
        f=open(file,'r')
        md5 = hashlib.md5()
        for chunk in iter(lambda: f.read(8192), b''):
            md5.update(chunk)
        f.close()
        return md5.hexdigest()
    except:
        return None

def checkhashes():
    allgood=0
    print "[+]Scanning files from hashfile %s" % sys.argv[1]
    hashfile=open(sys.argv[1],'r')
    for line in hashfile.readlines():
        oldhash,file=line.strip().split(',')
        if os.path.basename(file).startswith("md5s") == True : continue
        actualhash=md5_file(file)
        if actualhash==None:
            print "[!]File has been deleted: %s" % file
        elif oldhash != actualhash:
            print "[!]File has changed: %s" % file
            print "   Old chesksum:" + oldhash
            print "   New checksum:" + actualhash
            allgood+=1
    hashfile.close()
    if allgood == 0: print "[+]No files changes"
    else: print "[!] %d file's has been changed!" % allgood

def makehashes():
    filename="md5s"+time.strftime("%Y-%m-%d-%H%M")+".txt"
    print "[+]No hashfile provided, creating new list\n-->" + filename
    hashfile=open(filename, "w+")
    for path, subFolders, files in os.walk(dir):
        for file in files:
            sys.stdout.write("    [-]"+os.path.join(path,file))
            hash=md5_file(os.path.join(path,file))
            print " - " + hash
            hashfile.write(hash+","+os.path.join(os.path.abspath(path),file+"\n"))
    hashfile.close()

try:
    dir=os.path.join(sys.argv[1]) #directory provided
except:
    dir=os.getcwd() #no directory provided (use current working dir)

if os.path.isfile(os.path.join(dir)) == True: #file provided, run checkhashes
    os.path.isfile(os.path.join(dir))
    checkhashes()
else:
    #directory provided, run makehashes
    makehashes()
