import os, sys


def count_files(file_extension):
    count = 0
    for root, dirs, files in os.walk('./'):
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension == file_extension:
                count += 1
    print(count)
    return count



def main():
    count_files(sys.argv[1])


if __name__ == '__main__':
    main()
