def mean(num):
    return sum(int(i) for i in str(num)) / len(str(num))


print(mean(123))