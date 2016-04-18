'''
Created on Mar 30, 2016
userpw version 1.0
@author: RandyGuo

version 2.0 goals 
1. Enhanced: hide the password when add a new user
2. Restrict the login times , if try 5 password ,even can not login ,then exit the login console.
'''
#!/usr/bin/env python

db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = input(prompt)
        if name in db.keys(): #dict.has_key has been removed in Python 3.0, use in instead
            prompt = 'name taken,try another: '
            continue
        else :
            break
    pwd = input('password: ')
    db[name] = pwd
            
def olduser():
    name = input('login: ')
    EnterTimes = 0
    # Check the user whether created or not.
    if name not in db.keys():
        while EnterTimes < 5:
            if name in db.keys():
                break
            EnterTimes += 1
            print('The user you entered is not existed,please try the correct user\n')
            #print("Try times : ",EnterTimes)
            name = input('login: ')
        print('You have tried 5 time , reture to menu!')
        showmenu()
    #Check if the password enter correctly.
    pwd = input('password: ')
    passwd = db.get(name)
    EnterTimes = 0
    if passwd == pwd:
        print('Welcome Back', name)
    else :
        PassState = False
        while EnterTimes < 5:
            if passwd == pwd :
                print('Welcome Back : ',name)
                PassState = True
                break
            else :
                EnterTimes += 1
                pwd=input('The invalid password you enter, try again: ')
        if not PassState:
            print('You have tried 5 time , reture to menu!')
            showmenu()     
    
def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter Choice: """

    done = False
    while not done:
        
        chosen = False
        while not chosen:
            try:
                choice= input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice = 'q'
            print('\n You picked: [%s]' % choice)
            if choice not in 'neq':
                print('Invalid option,try again')
            else:
                chosen = True
        if choice == 'q':
            done = True
            print('Goodbye!!')
        if choice == 'n':newuser()
        if choice == 'e':olduser()
    
        
if __name__ == '__main__':
    showmenu()