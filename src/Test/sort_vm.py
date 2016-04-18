'''
Created on Apr 15, 2016

@author: Administrator
'''

BlockAndAssigned = open("D:/PythonExcise/blockandassigned.txt",'r')
vm_name = open("D:/PythonExcise/vm_name.txt",'w')
vm_name_list = []
for line in BlockAndAssigned:
    vm_name_list.append(line.split(',')[1])
    print(line.split(',')[1])
vm_name_list.sort()
for vm in vm_name_list:
    vm_name.write(vm)
    vm_name.write('\n')

BlockAndAssigned.close()
vm_name.close()