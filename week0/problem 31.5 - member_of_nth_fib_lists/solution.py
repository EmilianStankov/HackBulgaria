def member_of_nth_fib_lists(listA, listB, needle):
	a = listA
	b = listB
	index = 2
	is_member = False

	while index <= len(needle):
		next = a + b
		a = b
		b = next
		index += 1
		if b == needle:
			is_member = True
			break
		else:
			is_member = False

	return is_member
