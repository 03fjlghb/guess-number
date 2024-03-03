import random
r = random.randint(1, 100)

count = 0

while True:
	count = count + 1
	a = input('給你1~100的範圍,猜猜看我在想哪個數字~  ')
	i_a = int(a)
	if i_a == r:
		print('終於猜對了!')
		break
	elif i_a > r:
		print('比這個再小喔!')
	else:
		print('比這個再大喔!')
	print('這是你猜的第', count, '次了喔')