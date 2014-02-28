from collections import OrderedDict
from operator import itemgetter


def sort_fractions(fractions):
    ordered_fractions = []
    fractions_dict = {}
    ordered_fractions_dict = {}

    for fraction in fractions:
        fractions_dict[fraction] = fraction[0] / fraction[1]

    ordered_fractions_dict = OrderedDict(sorted(fractions_dict.items(), key = itemgetter(1)))

    for fraction in ordered_fractions_dict:
        ordered_fractions.append(fraction)

    return ordered_fractions


def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))


main()
