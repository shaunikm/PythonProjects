def sort_by_length(lst):
    return sorted(lst, key=len)


print(sort_by_length(["a", "ccc", "dddd", "bb"]))