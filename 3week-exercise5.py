def letter_e_checker():
	
	str = "next people"
	counter = 0
	
	for count in str:
		if count == 'e':
			counter = counter+1
			
	return counter
			
print (letter_e_checker())