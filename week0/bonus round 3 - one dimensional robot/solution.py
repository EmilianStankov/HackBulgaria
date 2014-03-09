def final_position(commands, a, b):
	position = 0
	for char in commands:
		if char == 'R' and position < b:
			position += 1
		elif char == 'L' and position > -a:
			position -= 1

	return position
