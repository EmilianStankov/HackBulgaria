def sum_of_digits(n):
    sum = 0
    if(n < 0):
        n = abs(n)
    num_str = str(n)
    for i in range(len(num_str)):
        sum += int(num_str[i])
    return sum
