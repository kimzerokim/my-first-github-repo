def reverse_check(string):

	for counter in range(len(string)):

		if (string[counter] != string [len(string)-(1+counter)]):
			
			return 'different'
		
	return 'same'


print('start test')

print(reverse_check('refer'))
print(reverse_check('aha'))

print(reverse_check('test'))
print(reverse_check('prefer'))