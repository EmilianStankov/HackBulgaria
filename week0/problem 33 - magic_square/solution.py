def magic_square(matrix):
	forward_main_diag = 0
	backward_main_diag = 0
	columns_sum = 0
	rows_sum = 0
	columns = [0] * int(len(matrix))
	rows = [0] * len(matrix)
	is_magic_square = False

	for i in range(len(matrix)):
		forward_main_diag += matrix[i][i]
		backward_main_diag += matrix[len(matrix) - i - 1][i]
		for j in range(len(matrix)):
			columns[j] += matrix[i][j]
			rows[j] += matrix[j][i]

	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if columns[i] != columns[j]:
				break
			else:
				columns_sum = columns[0]

			if rows[i] != rows[j]:
				break
			else:
				rows_sum = rows[0]

	if rows_sum == columns_sum == backward_main_diag == forward_main_diag:
		is_magic_square = True
	else:
		is_magic_square = False

	return is_magic_square
