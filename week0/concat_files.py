import sys


def main():
    MEGATRON = "MEGATRON.txt"
    to_write = ""
    for i in range(1, len(sys.argv)):
        filename = ""
        file = ""
        content = ""
        filename = sys.argv[i]
        file = open(filename, 'r')
        content = file.read()
        to_write += content
        file.close()

    new_file = open(MEGATRON, 'w')
    print(to_write)
    new_file.write(to_write)

    new_file.close()


if __name__ == '__main__':
    main()
