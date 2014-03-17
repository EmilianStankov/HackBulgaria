import sys


def cat2():
    content = []
    for i in range(1, len(sys.argv)):
        filename = ""
        file = ""
        filename = sys.argv[i]
        file = open(filename, 'r')
        file_contents = file.read()
        content.append(file_contents)
        file.close()
    return '\n\n'.join(content)


def main():
    print(cat2())


if __name__ == '__main__':
    main()
