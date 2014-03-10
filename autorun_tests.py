import os
from subprocess import call


def locate_and_run(pattern):
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.startswith(pattern):
                call(['py', root + '/' + file])


def main():
    locate_and_run('tests')


if __name__ == '__main__':
    main()
