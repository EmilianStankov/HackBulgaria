def biggest_difference(arr):
	biggest = 0
	for i in arr:
		for j in arr:
			if i != j and i - j <= biggest:
				biggest = i - j
	return biggest
