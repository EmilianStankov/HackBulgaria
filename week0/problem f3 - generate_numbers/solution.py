import sys
from random import randint


def main():
    filename = sys.argv[1]
    length = int(sys.argv[2])
    file = open(filename, 'w')
    for i in range(length):
        file.write(str(randint(1, 1000)))
        file.write(" ")
    print(filename, length)
    file.close()

if __name__ == '__main__':
    main()
