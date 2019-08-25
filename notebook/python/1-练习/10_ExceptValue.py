
import math

for i in range(10):
	try:
		input_number = input('write number: ')
		if input_number == 'q':
			break
		result = math.log(float(input_number))
		print(result)
	except ValueError:
		print('ValueError input must > 0')
	
