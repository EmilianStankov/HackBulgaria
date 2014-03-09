def contains_digit(number, digit):
	contains_digit = False
	num_str = str(number)
	for i in num_str:
		if str(digit) == i:
			contains_digit = True
			break
		else:
			contains_digit = False
	return contains_digit
