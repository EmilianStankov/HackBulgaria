import sys


def cat():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        file = open(filename, 'r')
        content = file.read()
        file.close()
        return content
