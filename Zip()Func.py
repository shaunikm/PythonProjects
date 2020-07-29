def convert_cartesian(x, y):
    a = []
    for z, n in zip(x, y):
        a.append([z, n])
    return a


print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]))