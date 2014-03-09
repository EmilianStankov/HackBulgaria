from collections import OrderedDict


def count_words(arr):
    words = {}
    ordered_words = {}
    count = 0
    for word in arr:
        current = str(word)
        for other_word in arr:
            if current == str(other_word):
                count += 1
        words[current] = count
        current = ""
        count = 0
    ordered_words = OrderedDict(sorted(words.items(), key = lambda t: t[0]))
    return ordered_words
