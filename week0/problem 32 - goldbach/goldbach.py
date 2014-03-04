def is_prime(n):
	isPrime = False
	if n == 1:
		isPrime = False
	if n == 2:
		isPrime = True
	for i in range(1, n + 1):
		if i != 1 and i != n:
			if n % i == 0:
				isPrime = False
				break
			else:
				isPrime = True
	return isPrime


def goldbach(n):
	goldbach = []
	for i in range(n):
		if is_prime(i) == True and is_prime(n - i) == True:
			goldbach.append((i, n - i))
	for each in goldbach:
		for each_other in goldbach:
			if each[0] == each_other[1] and goldbach.index(each) != goldbach.index(each_other):
				del goldbach[goldbach.index(each_other)]
	return goldbach


def main():
	print(goldbach(4))
	print(goldbach(6))
	print(goldbach(8))
	print(goldbach(10))
	print(goldbach(100))


main()