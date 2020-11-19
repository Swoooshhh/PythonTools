#To ask who to search
who = input('Who would you like to search?') 
#Open iplist.txt which contains the names and IP addresses
with open("iplist.txt") as ip:
	for line in ip.readlines():
		if who in line:
			print( line )
#Ask if they would like to add anyone.
add = input('Would you like to add anyone? y/n ')
if add == "y":
	newname = input('Name: ')
	newip = input('IP: ')
	with open('iplist.txt',mode='r+') as ip_write:
		ip_write.write(f'\n{newname} {newip}')
else:
	pass
