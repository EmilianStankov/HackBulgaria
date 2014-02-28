def is_an_bn(word):
    new_word = 'a' * int(len(word) / 2) + 'b' * int(len(word) / 2)
    if word == new_word:
        return True
    else:
        return False


def main():
    print(is_an_bn(""))
    print(is_an_bn("rado"))
    print(is_an_bn("aaabb"))
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("bbbaaa"))
    print(is_an_bn("aaaaabbbbb"))


main()
