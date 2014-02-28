def nth_fib_lists(listA, listB, n):
	a = listA
	b = listB
	index = 2

	while index <= n:
		next = a + b
		a = b
		b = next
		index += 1
	
	return a


def main():
	print(nth_fib_lists([1], [2], 1))
	print(nth_fib_lists([1], [2], 2))
	print(nth_fib_lists([1, 2], [1, 3], 4))
	print(nth_fib_lists([], [1, 2, 3], 4))
	print(nth_fib_lists([], [], 100))


main()