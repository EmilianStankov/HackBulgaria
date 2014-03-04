def number_to_list(n):
	l = []
	num_str = str(n)
	for i in num_str:
		l.append(int(i))
	return l


def main():
	print(number_to_list(123))
	print(number_to_list(99999))
	print(number_to_list(123023))


main()