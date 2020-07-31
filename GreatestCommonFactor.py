#this code is meant to be simple and to get the GCF of any two numbers
#if you want to get the GCF of more numbers, you can modify the code to fit your needs

def GCF(x,y):
    g = 1 #set the GCF standard value
    for i in range(1, min(x, y) + 1): #go through every value in between 1 and the smallest number of x and y
        if x % i == 0 and y % i == 0: #check if the values are divisble
            g = max(i, g) #the GCF becomes greater if the value if i is greater than it
    return g #return the GCF

#main/test code
print(str(GCF(270, 195git)))