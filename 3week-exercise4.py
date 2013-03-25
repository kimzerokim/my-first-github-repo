import math

def lengthchecker(x1,y1,x2,y2):
	
	x_minus_sq = 0
	y_minus_sq = 0
	diagonal_length = 0
	
	x_minus_sq = (x1-x2)**2
	y_minus_sq = (y1-y2)**2
	
	diagonal_length = math.sqrt(x_minus_sq+y_minus_sq)
	
	return diagonal_length
	
x1 = input('x1 = ')
y1 = input('y1 = ')
x2 = input('x2 = ')
y2 = input('y2 = ')

print lengthchecker(x1,y1,x2,y2)