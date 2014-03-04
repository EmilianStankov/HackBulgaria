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


def main():
	print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
	print(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]))
	print(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]))
	print(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]))


main()