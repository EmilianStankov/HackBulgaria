def prepare_meal(number):
    if number % 5 != 0:
        for n in range(number):
            if number % 3 ** n:
                return ('spam ' * (n - 1)).strip()

    else:
        for n in range(number):
            if number % 3 ** n:
                return 'spam ' * (n - 1) + 'and eggs'
            elif number % 3 != 0:
                return 'eggs'
