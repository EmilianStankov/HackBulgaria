def is_an_bn(word):
    new_word = 'a' * int(len(word) / 2) + 'b' * int(len(word) / 2)
    if word == new_word:
        return True
    else:
        return False
