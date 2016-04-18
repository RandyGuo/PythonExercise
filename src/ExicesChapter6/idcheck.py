'''
Created on Mar 31, 2016
excise 6_2 :修改例6-1的idcheck.py脚本，使之可以检测长度为一的标示符，并且可以识别关键字。
Python Version : Python 3.3.4
@author: RandyGuo
Date: 2016-03-31
'''
# this is a function to solve identify the id

import keyword
import string

alphas = string.ascii_letters + '_'
nums = string.digits
keywords = keyword.kwlist
alphnums = alphas + nums

def idcheck(identifier):
    if len(identifier) == 1:
        if identifier not in alphas:
            print('Invalid : first sybol must be alphabetic or "_" ')
        else:
            print('Okay as a legal identifier')
    else:
        if identifier in keywords:
            print('Invalid : identifier can not be a key word.')
        elif identifier[0] not in alphas:
            print('Invalid : first sybol must be alphabetic or "_"')
        else:
            for otherChar in identifier[1:]:
                if otherChar not in alphnums:
                    print('Invalid: remaining symbols must be alphanumeric!')
                    break
            else:
                print('Okay as a legal identifier')

def main():
    testIdentifier = ['1','1abc','a_123','_','a','break','for','For','adb  123']
    for identifier in testIdentifier:
        print("Check Identifier:",identifier)
        idcheck(identifier)
if __name__ == '__main__':
    print("welcome to program for check Identifier Version 2.0")
    main()