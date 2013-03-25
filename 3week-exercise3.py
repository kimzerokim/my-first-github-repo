def print_superpowernumber (num) :
	
	num = input('input some number  ')
	
	if (0 <= num | num < 10):
		return num + 10
	
	elif (10 <= num  | num <= 100):
		return num * 0.1
	
	else:
		return False
		
num = 0


print (print_superpowernumber(num))
	