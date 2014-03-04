import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    content = file.read()
    numbers = []
    to_append = ""
    sum = 0
    for symbol in content:
        if symbol != " ":
            to_append += symbol
        else:
            numbers.append(to_append)
            to_append = ""
    for each in numbers:
        sum += int(each)
    print(sum)

if __name__ == '__main__':
    main()
