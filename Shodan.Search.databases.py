#!/usr/bin/env python

from shodan import *
SHODAN_API_KEY = "API KEY HERE"
api = WebAPI(SHODAN_API_KEY)

def menu():
    print "**************************************"
    print "*     Shodan Search By Drx    *"
    print "**************************************"
    print
    print "[1] Search by subnet (add cidr value) ex:/24"
    print "[2] Search by hostname (ex: computing.site.com)"
    print "[3] Search for printers by organization (ex: Microsoft)"
    print "[4] Search for ports by organization (supported ports:http://www.shodanhq.com/help/filters#port)"
    print "[5] Seach Metasploit modules (useful if you find something good)
    print "[6] Exit script"
    print
    select_mod()

def select_mod():
    menu_select = raw_input("Please enter an option: ")
    if menu_select == "1":
        sub_search(api)
    elif menu_select == "2":
        host_search(api)
    elif menu_select == "3":
        print_search(api)
    elif menu_select == "4":
        port_search(api)
    elif menu_select == "5":
        sploit_search(api)
    elif menu_select == "6":
        exit()
    else:
        print "please enter a valid choice"
        menu()

def sub_search(api):
    res_out = open("NET-RESULTS.txt","a")
    prefix = "net:"
    query = raw_input("Enter Subnet (with cidr): ")
    data = prefix + query
    try:
        search_query = api.search(data)
        print 'Results found: %s' % search_query['total']
        for result in search_query['matches']:
            print >>res_out,"--START--" 
            print >>res_out,'IP: %s' % result['ip']
            print >>res_out,result['data']
            print >>res_out,result['hostnames']
            print >>res_out,result['port']
            print >>res_out,result['os']
            print >>res_out,result['updated']
            print >>res_out,"--END--"
            print >>res_out,""
            print >>res_out,""
        res_out.close()
        print "Results have been exported to: NET-RESULTS.txt"
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()

def host_search(api):
    res_out = open("HOST-RESULTS.txt","a")
    prefix = "hostname:"
    query = raw_input("Please enter hostname: ")
    data = prefix + query
    try:
        search_query = api.search(data)
        print 'Results found: %s' % search_query['total']
        for result in search_query['matches']:
            print >>res_out,"--START--" 
            print >>res_out,'IP: %s' % result['ip']
            print >>res_out,result['data']
            print >>res_out,result['hostnames']
            print >>res_out,result['port']
            print >>res_out,result['os']
            print >>res_out,result['updated']
            print >>res_out,"--END--"
            print >>res_out,""
            print >>res_out,""
        res_out.close()
        print "Results have been exported to: HOST-RESULTS.txt"
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()

def print_search(api):
    res_out = open("PRINTER-RESULTS.txt","a")
    prefix = "org:"
    query = raw_input("Please enter company/org: ")
    data = prefix + '"'+ query +'"'+" print"
    try:
        search_query = api.search(data)
        print 'Results found: %s' % search_query['total']
        for result in search_query['matches']:
            print >>res_out,"--START--" 
            print >>res_out,'IP: %s' % result['ip']
            print >>res_out,result['data']
            print >>res_out,result['hostnames']
            print >>res_out,result['port']
            print >>res_out,result['os']
            print >>res_out,result['updated']
            print >>res_out,"--END--"
            print >>res_out,""
            print >>res_out,""
        res_out.close()
        print "Results have been exported to: PRINTER-RESULTS.txt"
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()

def port_search(api):
    res_out = open("PORT-RESULTS.txt","a")
    prefix = "org:"
    query = raw_input("Please enter company/org: ")
    port_prefix = "port:"
    search_port = raw_input("Please enter the port: ")
    data = prefix + '"'+ query +'"'+ port_prefix + search_port
    try:
        search_query = api.search(data)
        print 'Results found: %s' % search_query['total']
        for result in search_query['matches']:
            print >>res_out,"--START--" 
            print >>res_out,'IP: %s' % result['ip']
            print >>res_out,result['data']
            print >>res_out,result['hostnames']
            print >>res_out,result['port']
            print >>res_out,result['os']
            print >>res_out,result['updated']
            print >>res_out,"--END--"
            print >>res_out,""
            print >>res_out,""
        res_out.close()
        print "Results have been exported to: PORT-RESULTS.txt"
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()

def sploit_search(api):
    res_out = open("METASPLOIT-RESULTS.txt","a")
    query = raw_input("Enter what you want to look for:")
    search_query = api.msf.search(query)
    print 'Metasploit Modules Found: %s' % search_query['total']
    try:
        for module in search_query['matches']:
            print >>res_out,'%s: %s' % (module['type'], module['name'])
        res_out.close()
        print "Results have been exported to: METASPLOIT-RESULTS.txt"
        menu()
    except Exception, e:
        print 'Error: %s' % e
        menu()            
menu()
