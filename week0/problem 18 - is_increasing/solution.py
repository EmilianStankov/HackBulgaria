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
