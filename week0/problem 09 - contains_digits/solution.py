def contains_digits(number, digits):
	contains_digits = []
	num_str = str(number)
	for j in range(len(digits)):
		for i in num_str:
			if str(digits[j]) == i:
				contains_digits.append('True')
				break
			else:
				pass
	if len(contains_digits) == len(digits) and len(digits) != 0:
		return True
	elif len(contains_digits) == 0:
		return True
	else:
		return False
