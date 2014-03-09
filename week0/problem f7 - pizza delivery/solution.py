from time import time
from datetime import datetime


def get_command(command, command_str, command_list):
    for i in range(len(command)):
        if command[i] != " ":
            command_str += command[i]
        else:
            command_list.append(command_str)
            command_str = ""
            
        if i == len(command) - 1:
            command_list.append(command_str)
            command_str = ""

def take(person, price, content):
    if person not in content.keys():
        content[person] = float(price)
        print("Taking order from", person, "for", price)
    else:
        content[person] += float(price)
        content[person] = round(content[person], 2)
        print("Taking order from", person, "for", price)


def status(content):
    for key in content:
        print(key + " - " + str(content[key]))


def save(content, saves_list):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filename = "orders_" + stamp
    file = open(filename, 'w')

    for key in content:
        file.write(key + " - " + str(content[key]) + '\n')

    file.close()
    saves_list.append(filename)
    saves_list.sort()
    saves_list.reverse()


def list(saves_list):
    for element in saves_list:
        print('[' + str(saves_list.index(element) + 1) + ']' + " - " + str(element) + '\n')


def load(saves_list, command_list, content):
    filename = saves_list[int(command_list[1]) - 1]
    file = open(filename, 'r')
    file_content = file.read()
    row = ""
    rows = []
    key = ""
    value = ""

    for i in range(len(file_content)):
        if file_content[i] != '\n':
            row += file_content[i]
        else:
            rows.append(row)
            row = ""

    for i in range(len(rows)):
        for j in range(len(rows[i])): 
            if rows[i][j] != " ":
                key += rows[i][j]
                for k in range(j, len(rows[i])):
                    if rows[i][k] != " ":
                        value += rows[i][k]
                    else:
                        value = ""
            else:
                content[key] = float(value)
                value = ""
                key = ""
                break

    file.close()


def error_message():
    print("Unknown command!")
    print("Try one of the following:")
    print("take <name> <price>")
    print("status")
    print("save")
    print("list")
    print("load <number>")
    print("finish")


def main():
    order_content = {}
    saves_list = []
    command = ""
    while command != 'finish':
        command = input("Enter command>")
        command_str = ""
        command_list = []
        get_command(command, command_str, command_list)

        if command_list[0] == 'take':
            take(command_list[1], command_list[2], order_content)

        elif command_list[0] == 'status':
            status(order_content)

        elif command_list[0] == 'save':
            save(order_content, saves_list)

        elif command_list[0] == 'list':
            list(saves_list)

        elif command_list[0] == 'load':
            order_content = {}
            load(saves_list, command_list, order_content)

        elif command_list[0] == 'finish':
            print("You have not saved your order.")
            print("If you wish to continue, type finish again.")
            print("If you want to save your order, type save")
            command_list[0] = input("Enter command>")
            if command_list[0] == 'finish':
                print('Finishing order. Goodbye!')
            elif command_list[0] == 'save':
                save(order_content, saves_list)

        else:
            error_message()


if __name__ == '__main__':
    main()