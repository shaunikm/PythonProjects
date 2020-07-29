john = True

input_num = input("How many letters do you want to move backwards? ")
print("\n")
string = input("What word do you want to do this to? ")
string_len = len(string)
stringbpi = string[0: int(input_num)]
string_print = (int(string_len) - int(input_num)) * -1

if int(input_num) > string_len:
    print("\nInput number too large")
    john = False

if " " in string:
    print("\nCannot do this with two or more words")

if " " not in string and john is True and int(input_num) != int(string_len):
    print("\n")
    print(string[int(string_print):] + string[0: int(input_num)])

elif " " not in string and int(input_num) > 1 and john is True and int(input_num) == int(string_len):
    print("\n")
    print(string)