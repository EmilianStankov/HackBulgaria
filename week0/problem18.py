def is_increasing(seq):
	is_increasing = False
	for element in seq:
		if len(seq) == 1:
			is_increasing = True
			break

		if seq.index(element) < len(seq) - 1:
			if element < seq[seq.index(element) + 1]:
				is_increasing = True
			else:
				is_increasing = False
				break

	return is_increasing


def main():
	print(is_increasing([1,2,3,4,5]))
	print(is_increasing([1]))
	print(is_increasing([5,6,-10]))
	print(is_increasing([1,1,1,1]))


main()