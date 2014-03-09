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
