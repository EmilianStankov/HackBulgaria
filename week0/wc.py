import sys


def main():
    filename = sys.argv[2]
    file = open(filename, 'r')
    content = file.read()
    chars = 0
    words = []
    lines = 1
    to_append = ""
    if sys.argv[1] == 'chars':
        for i in range(len(content)):
            chars += 1
        print(chars)
    elif sys.argv[1] == 'words':
        for symbol in content:
            if symbol != " " and symbol != "\n":
                to_append += symbol
            else:
                if to_append != "":
                    words.append(to_append)
                    to_append = ""

        if to_append != "":
            words.append(to_append)
        print(len(words))
    elif sys.argv[1] == 'lines':
        for symbol in content:
            if symbol == '\n':
                lines += 1
        print(lines)


if __name__ == '__main__':
    main()
