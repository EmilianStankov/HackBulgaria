def is_int_palindrom(n):
    s = str(n)[::-1]
    if s == str(n):
        return True
    else:
        return False

