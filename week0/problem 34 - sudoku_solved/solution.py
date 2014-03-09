def sudoku_solved(sudoku):
	columns_sum = 0
	rows_sum = 0
	columns = [] * 9
	rows = [0] * 9
	is_solved = False
	subsquares = [0] * 9
	needed = [[1, 2, 3, 4, 5, 6, 7, 8, 9]] * 9
	sudoku_list = []

	for i in range(9):
		sudoku_list += sudoku[i]
		for j in range(9):
			columns.append(sudoku[j][i])

	for i in range(82):
		if i < 10:
			columns[i] = columns[i * 9:i * 9 + 9]
		else:
			columns.pop()

	for j in range(9):
		if j < 3:
			c = 0
		elif j >= 3 and j < 6:
			c = 18
		else:
			c = 36
		subsquares[j] = (
			sudoku_list[j * 3 + c:j * 3 + 3 + c]
			+ sudoku_list[j * 3 + 9 + c:j * 3 + 12 + c]
			+ sudoku_list[j * 3 + 18 + c:j * 3 + 21 + c]
		)

	for i in range(9):
		rows[i] = sorted(sudoku[i])
		columns[i] = sorted(columns[i])
		subsquares[i] = sorted(subsquares[i])

	if subsquares == columns == rows == needed:
		is_solved = True
	else:
		is_solved = False

	return is_solved
