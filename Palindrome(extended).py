import time

print("This program checks to see if a number is a palindrome and is a loop.")
time.sleep(2)

john = True
palindrome_backwards = []
palindrome_backwards_real = ""


def list_(s, z):
    for x in s:
        z += x

    return z


while john is True:
    palindrome_backwards_real = ""
    palindrome_check = input("Enter a string in: ")

    i = len(palindrome_check)

    while i > 0:
        palindrome_backwards += str(palindrome_check[i - 1])
        i = i - 1

    palindrome_backwards_real = list_(palindrome_backwards, palindrome_backwards_real)

    if palindrome_backwards_real == palindrome_check:
        print("This is a palindrome.")
        time.sleep(3)
        print(50 * "\n")
    elif palindrome_backwards_real != palindrome_check:
        print("This is not a palindrome.")
        time.sleep(2)
        print(50 * "\n")