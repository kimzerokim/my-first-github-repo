def abs_val(num):
	
	num = input("input num = ")

	if (num == 0):
		return 0

	elif (num < 0):
		return (-num)

	else:
		return num

num = 0

print (abs_val(num))