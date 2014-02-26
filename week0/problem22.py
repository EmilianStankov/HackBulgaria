from math import floor

def calculate_coins(sum):
	coin_values = [100, 50, 20, 10, 5, 2, 1]
	answer = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
	new_sum = round(sum * 100)
	print(new_sum)
	for value in coin_values:
		if new_sum / value >= 1:
			answer[value] = floor(new_sum / value)
			new_sum -= floor(new_sum / value) * value
	return answer


def main():
	print(calculate_coins(0.53))
	print(calculate_coins(8.94))
	print(calculate_coins(16.58))


main()