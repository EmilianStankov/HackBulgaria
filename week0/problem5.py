def prime_number_of_divisors(n):
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)

    divisors = len(a)
    if divisors == 1:
        isPrime = False
    if divisors == 2:
        isPrime = True
    for i in range(1, divisors + 1):
        if i != 1 and i != divisors:
            if divisors % i == 0:
                isPrime = False
                break
            else:
                isPrime = True
    return isPrime
