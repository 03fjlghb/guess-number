import random

i_min = input('請輸入範圍最小值(整數): ')
i_max = input('請輸入範圍最大值(整數): ')
i_min = int(i_min)
i_max = int(i_max)
r = random.randint(i_min, i_max)

count = 0

while True:
	count = count + 1
	a = input('範圍內,猜猜看我在想哪個數字~  ')
	i_a = int(a)
	if i_a == r:
		print('終於猜對了!')
		break
	elif i_a > r:
		print('比這個再小喔!')
	else:
		print('比這個再大喔!')
	print('這是你猜的第', count, '次了喔')