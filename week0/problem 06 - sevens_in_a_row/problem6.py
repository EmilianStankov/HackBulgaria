def sevens_in_a_row(arr, n):
    has_sevens = False
    new_arr = []
    for item in range(len(arr)):
        if arr[item] == 7:
            new_arr.append(arr[item])
            if item + n < len(arr):
                for i in range(item + 1, item + n):
                    if arr[i] != 7:
                        has_sevens = False
                        break
                    else:
                        new_arr.append(arr[i])
                if new_arr.count(7) >= n:
                    has_sevens = True
                    break
                else:
                    has_sevens = False
        new_arr = [] 
        
    return has_sevens


def main():
    print(sevens_in_a_row([1, 7, 7, 7, 0, 2], 3))
    print(sevens_in_a_row([7, 9, 7, 7, 0, 2], 3))
    print(sevens_in_a_row([7, 9, 7, 7, 7, 0, 2], 3))
    print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
    print(sevens_in_a_row([1, 7, 1, 7, 7], 4))
    print(sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
    print(sevens_in_a_row([7, 2, 1, 6, 2], 1))

main()
