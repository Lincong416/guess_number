import random
ran = random.randint(1,100)
x = 1
while True:
	num = input('Please guess a number from 1 to 100 inclusively')
	num = int(num)
	if num == ran:
		print('That is correct! Congretulation!')
		print('you have guessed', x, 'times')
		break
	elif num > ran :
		print('Wrong number! Correct number is smaller.')
	elif num < ran :
		print('Wrong number! Correct number is bigger.')
	print('you have guessed', x, 'times')
	x += 1