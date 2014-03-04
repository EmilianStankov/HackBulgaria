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


def main():
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(8))
    print(is_prime(11))
    print(is_prime(-10))


main()