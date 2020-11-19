who = input('Who would you like to search? no caps ')
def ipwriterr():
	newname = input('name: ')
	newip = input('ip: ')
	with open('test.txt',mode='a') as ip_write:
		ip_write.write(f"\n{newname} {newip}")

with open("test.txt") as ip:
	for line in ip.readlines():
		if who in line:
			print( line )
			ip.seek(0)


add = input('Would you like to add anyone? y/n ')
if add == "y":
	ipwriterr()
elif add == "Y":
	ipwriterr()
else:
	pass
