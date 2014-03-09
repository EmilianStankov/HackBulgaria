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
