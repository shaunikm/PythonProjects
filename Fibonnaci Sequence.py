class Fibonnaci:
    def __init__(self, n):
        self.n = n

    def Fibonnaci_(self):
        if self.n == 1:
            return [0]
        elif self.n == 2:
            return [0, 1]
        else:
            s = []
            try:
                for i in range(1, self.n + 2):
                    if i == 1:
                        s.append(0)
                    elif i == 2:
                        s.append(1)
                    else:
                        s.append(int(s[-1] + s[-2]))
                return s
            except:
                print('\u001b[31mMemory Error\u001b[0m')

    def Fibonnaci_get(self):
        if self.n == 1:
            return 0
        elif self.n == 2:
            return 1
        else:
            s = []
            try:
                for i in range(1, self.n + 2):
                    if i == 1:
                        s.append(0)
                    elif i == 2:
                        s.append(1)
                    else:
                        s.append(int(s[-1] + s[-2]))
                return s[-1]
            except:
                print('\u001b[31mMemory Error\u001b[0m')


Fib = Fibonnaci(6)
print(Fib.Fibonnaci_())
print(Fib.Fibonnaci_get())