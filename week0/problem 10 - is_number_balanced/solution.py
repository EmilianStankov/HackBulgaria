def is_number_balanced(n):
	num_str = str(n)
	if len(num_str) % 2 != 0:
		left_str = num_str[0:len(num_str) // 2:1]
		right_str = num_str[len(num_str) // 2 + 1:len(num_str):1]
	else:
		left_str = num_str[0:len(num_str) // 2:1]
		right_str = num_str[len(num_str) // 2:len(num_str):1]
	left = 0
	right = 0
	for i in left_str:
		left += int(i)
	for i in right_str:
		right += int(i)
	if left == right:
		return True
	else:
		return False
