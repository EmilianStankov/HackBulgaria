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
