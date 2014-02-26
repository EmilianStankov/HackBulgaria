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
	else:
		return False


def main():
	print(contains_digits(402123, [0, 3, 4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	print(contains_digits(456, []))

main()