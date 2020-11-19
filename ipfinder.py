who = input('Who would you like to search for? ')
whob = False
def ipwriterr():
	newname = input('name: ')
	newip = input('ip: ')
	with open('iplist.txt',mode='a') as ip_write:
		ip_write.write(f"\n{newname} {newip}")

with open("iplist.txt") as ip:
	for line in ip.readlines():
		if who in line:
			whob = True
			print( line )
			ip.seek(0)

if whob == False:
	print(f"[-] Cannot find {who}.")


add = input('Would you like to add anyone to the list? y/N ')
if add == "y":
	ipwriterr()
elif add == "Y":
	ipwriterr()
else:
	pass
