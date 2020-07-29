def print_all_groups():
    k = 1
    s = ''
    z = 97
    while k != 7:
        while z != 102:
            s += str(k) + chr(z) + ', '
            z += 1
        if z == 101:
            z = 97
        k += 1
    s = s.strip()
    return s[:-1]


print(print_all_groups())