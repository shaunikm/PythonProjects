def pass_encryption(x):
    x = str(x.replace("a", "!"))
    x = str(x.replace("b", "#"))
    x = str(x.replace("c", "0"))
    print(x)

loop_start = "abc"

pass_encryption(loop_start)