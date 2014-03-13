import string_utils
import sys

def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    content = file.read()
    file.close()

    file = open(filename, 'w')
    new_content = string_utils.tabs_to_spaces(content, 4)
    file.write(new_content)
    file.close()


if __name__ == '__main__':
    main()
