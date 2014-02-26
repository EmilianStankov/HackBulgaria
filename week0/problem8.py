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


def main():
	print(contains_digit(123, 4))
	print(contains_digit(42, 2))
	print(contains_digit(1000, 0))
	print(contains_digit(12346789, 5))

main()