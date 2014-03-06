from time import time
from datetime import datetime
import os


def create(filename):
    if os.path.isfile(filename):
        print('You already have a file for today it is: ' + filename)
    else:
        file = open(filename, 'w')
        file.close()
        print('New file created and loaded: ' + filename)


def change_date(command, stamp):
    command_list = command.split(" ")
    date = command_list[1].split("/")
    date.reverse()
    stamp = "_".join(date)
    filename = "attendance_" + stamp
    return(filename)


def add(command, filename):
    command_list = command.split(" ")
    person = command_list[1]
    is_enlisted = False
    if os.path.isfile(filename):
        file = open("students", 'r')
        for line in file:
            if line.rstrip() == person:
                is_enlisted = True
                break
        file.close()
        if is_enlisted == True:
            file = open(filename, 'r')
            for line in file:
                if line.rstrip() == person:
                    print(person + ' is already added to the list for today.')
                    file.close()
                    break
            else:
                file.close()
                file = open(filename, 'a')
                file.write(person + '\n')
                file.close()
                print(person + ' is now attending')
        else:
            print('That person is not a student here.')
    else:
        print('Please create or load a file first.')


def list():
    saves_list = []
    for root, dirs, files in os.walk('./'):
        for file in files:
            if file.startswith('attendance_'):
                saves_list.append(file)
    saves_list.sort()
    saves_list.reverse()
    return(saves_list)


def load(saves_list, command):
    command_list = command.split(" ")
    save_index = command_list[1]
    filename = saves_list[int(save_index) - 1]
    return filename


def status(filename):
    file = open(filename, 'r')
    content = file.readlines()
    for line in content:
        print(line.rstrip())


def statistic(saves_list):
    for save in saves_list:
        students = 0
        file = open(save, 'r')
        content = file.readlines()
        for line in content:
            students += 1
        print(save[11:] + ' - ' + str(students) + ' people attending from total of 43')


def error():
    print('Not a valid command, please enter one of the following:')
    print(' - create')
    print(' - change_date')
    print(' - add <name>')
    print(' - list')
    print(' - load')
    print(' - status')
    print(' - statistic')


def main():
    saves_list = list()
    command = ""
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
    filename = "attendance_" + stamp
    while command != 'finish':
        command = input("Enter command>")
        if command.startswith('create') == True:
            create(filename)
        elif command.startswith('change_date') == True:
            change_date(command, stamp)
            filename = change_date(command, stamp)
        elif command.startswith('add') == True:
            add(command, filename)
        elif command.startswith('list') == True:
            list()
            for save in saves_list:
                print('[' + str(saves_list.index(save) + 1) + '] - ' + save)
        elif command.startswith('load') == True:
            filename = load(saves_list, command)
        elif command.startswith('status') == True:
            status(filename)
        elif command.startswith('statistic') == True:
            statistic(saves_list)
        else:
            error()


if __name__ == '__main__':
    main()
