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


def simplify_fraction(fraction):
    new_fraction = [0, 0]
    new_fraction[0] = int(fraction[0])
    new_fraction[1] = int(fraction[1])
    for i in range(1, fraction[1] + 1):
        if is_prime(i) == True and fraction[1] % i == 0 and fraction[0] % i == 0:
            new_fraction[0] = int(fraction[0] / i)
            new_fraction[1] = int(fraction[1] / i)
            for j in range(i, fraction[1] + 1):
                if fraction[1] % j == 0 and fraction[0] % j == 0:
                    new_fraction[0] = int(fraction[0] / j)
                    new_fraction[1] = int(fraction[1] / j)
    new_tuple = (new_fraction[0], new_fraction[1])
    return new_tuple
