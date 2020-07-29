def j(lst):
    lst.append(lst[:])
    return lst


lst = [1, 2, 3]

k = j(lst)
print(k)