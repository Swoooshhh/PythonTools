who = input('Who would you like to search? no caps ')

with open("test.txt") as ip:
	for line in ip.readlines():
		if who in line:
			print( line )
		#else:
			#print('nothing found')


add = input('Would you like to add anyone? y/n ')
if add == "y":
	newname = input('name: ')
	newip = input('ip: ')
	with open('test.txt',mode='r+') as ip_write:
		ip_write.write(f'\n{newname} {newip}')
else:
	pass
