import time
print("This program checks to see if a number is a palindrome and is a loop.")
time.sleep(2)

john = True
i = -1

while john is True:
    palindrome_check = input("Enter a string in: ")

    palindorm_backwards = palindrome_check[::-1]

    if palindorm_backwards == palindrome_check:
        print("This is a palindrome.")
        time.sleep(3)
        print(50 * "\n")
    elif palindorm_backwards != palindrome_check:
        print("This is not a palindrome.")
        time.sleep(2)
        print(50 * "\n")
