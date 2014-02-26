def list_to_number(digits):
	num_str = ''
	for digit in digits:
		num_str += str(digit)
	return int(num_str)


def main():
	print(list_to_number([1,2,3]))
	print(list_to_number([9,9,9,9,9]))
	print(list_to_number([1,2,3,0,2,3]))

main()
