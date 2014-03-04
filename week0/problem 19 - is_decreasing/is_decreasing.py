def is_decreasing(seq):
	is_decreasing = False
	for element in seq:
		if len(seq) == 1:
			is_decreasing = True
			break

		if seq.index(element) < len(seq) - 1:
			if element > seq[seq.index(element) + 1]:
				is_decreasing = True
			else:
				is_decreasing = False
				break

	return is_decreasing


def main():
	print(is_decreasing([5,4,3,2,1]))
	print(is_decreasing([1,2,3]))
	print(is_decreasing([100, 50, 20]))
	print(is_decreasing([1,1,1,1]))


main()