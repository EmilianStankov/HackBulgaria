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

	return is_magic_square, columns, rows

def main():
	print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
	print(magic_square([[4,9,2], [3,5,7], [8,1,6]]))
	print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
	print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
	print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))


main()