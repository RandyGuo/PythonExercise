'''
Created on Apr 15, 2016
Test connect 
@author: Administrator
'''
import os

def check_IP_connect(IP_Segments):
    "please give the IP segent like this '9.115.208.22-253,9.115.209.2-112'"
    Blocked_IPs=open("D:/PythonExcise/Blocked_IPs.txt",'w')
    Blocked_IPNums = 0

#Check Which IP can not connect
    for IPs in IP_Segments:
        First_IP_Position = IPs.find('-') # IPs[:end] = 9.112.228.20
        IP_start = IPs[:First_IP_Position].split('.')[-1]     #['9','112','228','20'] -> 20
        IP_Split = IPs[:First_IP_Position].split('.')
        Prefix_IP = '.'.join(IPs[:First_IP_Position].split('.')[:-1])
        print("prefix IP: ",Prefix_IP)
        last_IP = IPs[First_IP_Position + 1:]
        print("first IP %s , end IP %s " % (IPs[:First_IP_Position],last_IP))
        #General IPS
        start = int(IP_start)
        end = int(last_IP)
        print("IP Segment Start at : %d and end at : %d" % (start,end))
        print("Start IP Position: ",IP_start)
        for IP in range(start,end+1):
            IP_Split[-1] = str(IP)
            ip_address = '.'.join(IP_Split)
            cmd = "ping %s " % ip_address
            #print(cmd)
            result = os.system(cmd)
            #print(result)
            if result == 0:
                print("%s can ping successfully!!" % ip_address)
            else:
                Blocked_IPNums += 1
                Blocked_IPs.write(ip_address)
                Blocked_IPs.write('\n')
    Blocked_IPs.write("The number of Blocked IP is : ")
    Blocked_IPs.write(str(Blocked_IPNums))
    Blocked_IPs.close()
    print(Blocked_IPNums)

if __name__ == '__main__':
    IP_Segments = ''' 9.112.228.20-161,9.112.229.170-254,9.112.230.27-254,9.112.235.71-100,9.112.248.20-29,9.110.182.124-133 '''.split(',')
    check_IP_connect(IP_Segments)