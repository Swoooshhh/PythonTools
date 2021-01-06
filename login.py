import json
import os
import hashlib
#I might add Hashed passwords and username changing if I remember
from getpass import getpass
class Login:
    def __init__(self):
        self.loggedin = False
        #self.storage = ''
    def signup(self):
        while True:
            username = input('What would you like to use as your username? 12 characters MAX. ')
            with open('items.json', 'r') as f:
                logincheck = json.load(f)
                if len(username) > 12:
                    print('Your username is too long.')
                    break
                elif username in logincheck:
                    for item in logincheck:
                        if username == item:
                            print(f"Sorry there is already another user named {item}")
                            break
                    break
                else:
                    print('Good choice.')
            newpassword = getpass('What would you like to use as your password? At least 6 characters')
            if len(newpassword) < 6:
                print('Your password is too short.')
                break
            with open('items.json', 'r') as f:
                fix = json.load(f)
            fix[str(username)] = newpassword
            with open('items.json', 'r+') as f:
                json.dump(fix, f, indent=4)
            print('Success.')
            break
    def login(self):
        while True:

            question = input('Would you like to do? \n 1: Signin\n 2: Signup\n 3: Change your username (Coming soon) \n 4: Change your password\n 5: Exit\n Selection: ')
            if question == '1':
                anotherquestion = input('Whats your Username? : ')
                anotheranotherquestion = getpass("What's your password? : ")
                with open('items.json', 'r') as logins:
                    logininfo = json.load(logins)
                    if anotherquestion in logininfo:
                        password = logininfo[anotherquestion]

                        if password == str(anotheranotherquestion):
                                print('Logged in')
                                self.loggedin = True
                                return False
                        else:
                            print('\nIncorrect username or password.\n')
                            break
                    else:
                        print('\nIncorrect username or password. \n')
                        break
            elif question == '2':
               Login().signup()
            elif question == '3':
                Login().changeusername()
            elif question == '4':
                Login().changepassword()
            elif question == '5':
                print('Bye! ')
                quit()
    def changepassword(self):
        while True:
            print('Please verify yourself.')
            anotherquestion = input('Whats your Username? : ')
            anotheranotherquestion = getpass("What's your password? : ")
            with open('items.json', 'r') as logins:
                logininfo = json.load(logins)
                if anotherquestion in logininfo:
                    password = logininfo[anotherquestion]
                    if password == anotheranotherquestion:
                        print('Logged in')
                        self.loggedin = True
                        break
                    else:
                        print('\nIncorrect username or password. \n')
                        break
                else:
                    print('\nIncorrect username or password. \n')
                    break
        while True:
            if self.loggedin == True:
                newpassword = getpass('What would you like to change your password to? At least 6 characters : ')
                if len(newpassword) < 6:
                    print('Password too short')
                    break
                elif password == newpassword:
                    print("You can't change your password to the same one you have now.")
                    break
                else:
                    print('Perfect!')
                with open('items.json', 'r') as f:
                    fix = json.load(f)
                fix[str(anotherquestion)] = newpassword
                with open('items.json', 'r+') as f:
                    json.dump(fix, f, indent=4)
                    print('Successfully changed password!')
                    break
    def changeusername(self):
        print('Unreleased...')
        # while True:
        #     print('\nPlease verify yourself.\n')
        #     anotherquestion = input('Whats your Username? : ')
        #     anotheranotherquestion = getpass("What's your password? : ")
        #     with open('items.json', 'r') as logins:
        #         logininfo = json.load(logins)
        #         if anotherquestion in logininfo:
        #             password = logininfo[anotherquestion]
        #             if password == anotheranotherquestion:
        #                 print('Logged in')
        #                 self.loggedin = True
        #                 break
        #             else:
        #                 print('\nIncorrect username or password. \n')
        #                 break
        #         else:
        #             print('\nIncorrect username or password. \n')
        #             break
        # if self.loggedin == True:
        #     newusername = getpass('What would you like to change your username to? : ')
        #     with open('items.json', 'r') as f:
        #         fix = json.load(f)
        #

            # username[str(anotherquestion)] = username[str(newusername)]
            #
            # with open('items.json', 'r+') as f:
            #     json.dump( f, indent=4)
            #     print('Successfully changed username!')



Login().login()
