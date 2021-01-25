import requests

class hostfile:
    def __init__(self):
        self.basic = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'
        self.familyprotect = 'https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/porn/hosts'
    def request(self,path, url):
        res = requests.get(url)
        data = res.text
        with open(path, 'w') as f:
            try:
                f.write(data)
            except OSError:
                print("Error writing. Run this as admin.")
    def choice(self):
        while True:
            choiced = input("What system do you use?\n 1. Linux \n 2. Windows \n 3. Mac OS (unreleased)\n > ")
            choicetwo = input('What kind of blocking would you like?\n 1. Basic ads, tracking and malware\n 2. Everything 1 has but adds family protections (blocks adult sites).\n > ')
            if choiced == '1':
                if choicetwo == '1':
                    try:

                        hostfile().request('/etc/hosts', self.basic)
                        print('Success!')
                        return False
                    except OSError:
                        print('Error writing. Run this as admin.')
                        return False
                elif choicetwo == '2':
                    try:

                        hostfile().request('/etc/host', self.familyprotect)
                        print('Success!')
                        return False
                    except OSError:
                        print("Error writing. Run this as admin.")
                        return False
                else:
                    print("Invalid option.")
            elif choiced == '2':
                if choicetwo == '1':
                    try:

                        hostfile().request('c:/windows/system32/drivers/etc/hosts', self.basic)
                        print('Success!')
                        return False
                    except OSError:
                        print('Error writing. Run this as admin.')
                        return False
                elif choicetwo == '2':
                    try:

                        hostfile().request('c:/windows/system32/drivers/etc/hosts', self.familyprotect)
                        print('Success!')
                        return False
                    except OSError:
                        print("Error writing. Run this as admin.")
                        return False
            elif choiced == '3':
                pass
hostfile().choice()
