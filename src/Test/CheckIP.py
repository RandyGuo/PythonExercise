'''
Created on Apr 15, 2016

@author: Administrator
'''

vm_infor = open('D:/PythonExcise/VM_Infor.csv','r').readlines()
IP_infor = open("D:/PythonExcise/Blocked_IPs.txt",'r').readlines()
BlockAndAssigned = open("D:/PythonExcise/blockandassigned.txt",'w')
blockedIP = open("D:/PythonExcise/blockAssignedip.txt",'w')
for ip in IP_infor:
    for vm in vm_infor:
        vm_list = vm.split(',')
        if ip[:-1] in vm_list:
            if vm_list[2] == 'Assigned':
                BlockAndAssigned.write(str(vm_list))
                blockedIP.write(ip[:-1])
                BlockAndAssigned.write('\n')
                blockedIP.write('\n')

BlockAndAssigned.close()
blockedIP.close()
#vm_infor.close()
#IP_infor.close()
