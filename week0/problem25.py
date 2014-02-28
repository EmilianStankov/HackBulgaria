def groupby(func, seq):
    dictionary = {}
    values = []
    for value in seq:
        for i in range(len(seq)):
            if func(value) == func(seq[i]):
                values.append(seq[i])
        dictionary[func(value)] = values
        values = []
    return dictionary


def main():
    print(groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
    print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
    print(groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))


main()
