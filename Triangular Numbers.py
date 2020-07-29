def triangle(n):
    i = 2
    f = 1
    z = 1
    if n == 1:
        pass
    while z < n and n != 1:
        f += i
        i += 1
        z += 1
    return f


n = input("Enter in a number: ")
n.strip()
z = triangle(int(n))
print("\nThis is the triangular number for your number: " + str(z))