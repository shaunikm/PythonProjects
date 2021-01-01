def add_indexes(lst):
    x = len(lst)
    f = 0
    while f < x:
        lst[f] = int(lst[f] + f)
        f += 1
    return lst


j = [5, 4, 3, 2, 1]
k = add_indexes(j)
print(k)
