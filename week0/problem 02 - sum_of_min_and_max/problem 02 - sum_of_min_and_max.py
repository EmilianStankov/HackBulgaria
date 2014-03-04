def sum_of_min_and_max(a):
    a.sort()
    return a[0] + a[len(a) - 1]
