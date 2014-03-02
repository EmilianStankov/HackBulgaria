from time import time
from datetime import datetime


def main():
    content = {}
    list = []
    command = ""
    saves = 0
    while command != 'finish':
        command = input("Enter command>")
        command_str = ""
        command_list = []

        for i in range(len(command)):
            if command[i] != " ":
                command_str += command[i]
            else:
                command_list.append(command_str)
                command_str = ""
            if i == len(command) - 1:
                command_list.append(command_str)
                command_str = ""

        if command_list[0] == 'take':
            if command_list[1] not in content.keys():
                content[command_list[1]] = float(command_list[2])
                print("Taking order from", command_list[1], "for", command_list[2])
            else:
                content[command_list[1]] += float(command_list[2])
                content[command_list[1]] = round(content[command_list[1]], 2)
                print("Taking order from", command_list[1], "for", command_list[2])

        elif command_list[0] == 'status':
            for key in content:
                print(key + " - " + str(content[key]))

        elif command_list[0] == 'save':
            saves += 1
            ts = time()
            stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            filename = "orders_" + stamp
            file = open(filename, 'w')
            for key in content:
                file.write(key + " - " + str(content[key]) + '\n')
            file.close()
            for i in range(saves + 1):
                if filename not in list:
                    list.append(filename)
            list.reverse()

        elif command_list[0] == 'list':
            for element in list:
                print('[' + str(list.index(element) + 1) + ']' + " - " + str(element) + '\n')

        elif command_list[0] == 'load':
            content = {}
            filename = list[int(command_list[1]) - 1]
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

        elif command == 'finish':
            print("You have not saved your order.")
            print("If you wish to continue, type finish again.")
            print("If you want to save your order, type save")
            command = input("Enter command>")
            if command == 'finish':
                print('Finishing order. Goodbye!')

        else:
            print("Unknown command!")
            print("Try one of the following:")
            print("take <name> <price>")
            print("status")
            print("save")
            print("list")
            print("load <number>")
            print("finish")


if __name__ == '__main__':
    main()