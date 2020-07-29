def first_and_last(s):
    a = []
    b = ''
    for c in sorted(s):
        b += c
    a.append(b)
    b = ''
    for d in sorted(s)[::-1]:
        b += d
    a.append(b)
    return a


l = 'john'
print(first_and_last(l))