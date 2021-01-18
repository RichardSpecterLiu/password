password = '520826'
x = 3
while True:
	a = input('Enter the password:')
	if a == password:
		print('Well, congratulations...did Richard tell you the password or are you a pure genius?')
		break
	else:
		x = x - 1 
		print('nope, you gotta', x ,'more chances.')
		if x == 0:
			while True:
				print('You gotta no more chances, dumbass!')




		
