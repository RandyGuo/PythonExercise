#!/usr/bin/env python
#This is a test code for some functions 

enterTimes = 0
while enterTimes < 5:
    name = input('login: ')
    if name == "randy" :
        break
    else:
        print("The user you enter is an invalid user, try again: ")
        enterTimes += 1
if enterTimes == 5:
    print('You have tried 5 times , Return the menu view')
        