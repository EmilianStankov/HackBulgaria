import sys


def main():
    for i in range(len(sys.argv)):
        if len(sys.argv) > 1:
            filename = ""
            file = ""
            content = ""
            filename = sys.argv[i]
            file = open(filename, 'r')
            content = file.read()
            print(content, '\n')


if __name__ == '__main__':
    main()
