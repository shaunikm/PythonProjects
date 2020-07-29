def left_digit(num):
    k = 0
    for char in num:
        if char.isdigit():
            k = int(char)
            break
        else:
            pass
    return k


num = "je2jfio3ouuuhdkmfioeiojehfij4o4y5o3 edy3"
k = left_digit(num)
print(k)