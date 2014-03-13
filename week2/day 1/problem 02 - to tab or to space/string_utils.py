def lines(text):
    return text.split('\n')


def unlines(elements):
    return '\n'.join(elements)


def words(text):
    return text.split()


def unwords(elements):
    return " ".join(elements)


def tabs_to_spaces(str, one_tab_n_spaces=4):
    return str.replace('\t', one_tab_n_spaces * ' ')
