'''
Created on Apr 15, 2016

@author: Administrator
'''

import os
ip_list = open("D:/PythonExcise/blockAssignedip.txt",'r')

def check_iplist(ip_list):
    for ip in ip_list:
        cmd = "ping %s " % ip[:-1]
        result=os.system(cmd)
        if result == 1:
            print("%s can not to be connect" % ip[:-1])

check_iplist(ip_list)