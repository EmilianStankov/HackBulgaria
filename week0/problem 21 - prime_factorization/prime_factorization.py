# i will use this function i wrote in problem 4
def is_prime(n):
    if n < 0:
        n = abs(n)
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


def prime_factorization(n):
	count = 0 # counter for the power of the prime factors
	number = 0 # the current prime factor
	tuples = [] # the list i am returning in the end
	for i in range(1, n + 1):
		if is_prime(i) == True:
			if n % i == 0:
				number = i
				count += 1
				# check how many times is the prime factor contained in the given number
				for j in (i ** x for x in range(1, n)):
					if n % (i * j) == 0:
						count += 1
				tuples.append((number, count)) # add the new tuple to the list
		count = 0 # reset the counter
	return tuples


def main():
	print(prime_factorization(10))
	print(prime_factorization(14))
	print(prime_factorization(356))
	print(prime_factorization(89))
	print(prime_factorization(1000))
	print(prime_factorization(17))
	print(prime_factorization(1024))


main()