import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        file = open(filename, 'r')
        content = file.read()
        print(content)

if __name__ == '__main__':
    main()
