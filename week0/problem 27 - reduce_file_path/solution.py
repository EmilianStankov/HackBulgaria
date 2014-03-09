def reduce_file_path(path):
    new_path = ""
    strings = []
    count = 0
    to_append = ""
    if path[0] == '/':
        for char in path:
            if char != '/':
                to_append += char
            elif char == '/' and to_append != "" or char == '':
                strings.append(to_append)
                to_append = ""
        if to_append != "":
            strings.append(to_append)
            to_append = ""

    for string in strings:
        for string in strings:
            for string in strings:
                if string == '' or string == '.':
                    del strings[strings.index(string)]
                elif string == '..' and len(strings) > 1:
                    del strings[strings.index(string) - 1]
                    del strings[strings.index(string)]
                elif string == '..' and len(strings) == 1:
                    del strings[strings.index(string)]

    for i in range(0, 2 * len(strings), 2):
        strings.insert(i, '/')
    if strings == []:
        strings = ['/']

    new_path = ''.join(strings)
    return new_path
