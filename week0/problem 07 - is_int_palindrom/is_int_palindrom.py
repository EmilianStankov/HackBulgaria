def is_int_palindrom(n):
    s = str(n)[::-1]
    if s == str(n):
        return True
    else:
        return False


def main():
    print(is_int_palindrom(1234321))
    print(is_int_palindrom(1234))
    print(is_int_palindrom(1))
    print(is_int_palindrom(42))
    print(is_int_palindrom(100001))
    print(is_int_palindrom(999))
    print(is_int_palindrom(123))

main()
