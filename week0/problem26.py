def prepare_meal(number):
    if number % 5 != 0:
        for n in range(number):
            if number % 3 ** n:
                return 'spam ' * (n - 1)

    else:
        for n in range(number):
            if number % 3 ** n:
                return 'spam ' * (n - 1) + 'and eggs'
            elif number % 3 != 0:
                return 'eggs'


def main():
    print(prepare_meal(3))
    print(prepare_meal(27))
    print(prepare_meal(7))
    print(prepare_meal(5))
    print(prepare_meal(15))
    print(prepare_meal(45))


main()
