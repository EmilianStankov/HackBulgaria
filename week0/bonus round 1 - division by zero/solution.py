def count_numbers(numbers):
	for number in numbers:
		for another_number in numbers:
			to_append = number // another_number
			if number > another_number and to_append not in numbers:
				numbers.append(to_append)
	
	return len(numbers)