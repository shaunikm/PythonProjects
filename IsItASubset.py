def is_subset(lst1, lst2):
    return True if all(x in lst2 for x in lst1) else False


print(is_subset([8, 5], [10, 5, 9, 6, 8]))