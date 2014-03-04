def biggest_difference(arr):
	biggest = 0
	for i in arr:
		for j in arr:
			if i != j and i - j <= biggest:
				biggest = i - j
	return biggest


def main():
	print(biggest_difference([1,2]))
	print(biggest_difference([1,2,3,4,5]))
	print(biggest_difference([-10, -9, -1]))
	print(biggest_difference(range(100)))

main()