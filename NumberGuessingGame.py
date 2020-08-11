import random
import math
import time


def get_factor(n):
    global lst
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst


def list_to_str(k):
    return ', '.join(str(i) for i in k)


def sum_of_digits(j):
    return sum(int(i) for i in str(j))


def guesses_so(*lo):
    global lst_
    if lo is None:
        return lst_
    else:
        lst_.append(', '.join(i for i in lo))
        return lst_


global lst
global lst_
lst = []
lst_ = []
jk = False
tu = False
z = False
b = random.randint(1, 100)
x = 50 * '\n'
g = 5
guess = ''
factors = get_factor(b)
if len(factors) > 3:
    random_factor = random.sample(factors[:-1], k=3)
    m = True
elif len(factors) == 3:
    random_factor = random.sample(factors[:-1], k=2)
    m = True
elif len(factors) == 2:
    random_factor = 1
    z = True
    m = True
else:
    tu = True
    m = True
hint4_1 = b - random.randint(10, 20)
hint4_2 = b + random.randint(10, 20)
hint4_1 = max(hint4_1, 1)
while m is True:
    if z is True:
        hint1 = 'The number is a prime number.'
    elif tu is True:
        hint1 = 'The number is a composite number.'
    else:
        hint1 = 'A few factors of your number are ' + str(list_to_str(random_factor)) + '.'
    if b % 2:
        hint2 = 'The number is an odd number.'
    else:
        hint2 = 'The number is an even number'
    if int(math.sqrt(b) + 0.5) ** 2 != b:
        hint3 = 'The number is not a square number.'
    else:
        hint3 = 'The number is a square number.'
    hint4 = 'The number is in the range of ' + str(hint4_1) + ' and ' + str(hint4_2) + '.'
    hint5 = 'The sum of the number\'s digits is ' + str(sum_of_digits(b)) + '.'
    if g == 5:
        print(hint5, end='                            ')
    elif g == 4:
        print(hint5)
        print(hint3, end='                            ')
    elif g == 3:
        print(hint5)
        print(hint3)
        print(hint1, end='                            ')
    elif g == 2:
        print(hint5)
        print(hint3)
        print(hint1)
        print(hint2, end='                            ')
    elif g == 1:
        print(hint5)
        print(hint3)
        print(hint1)
        print(hint2)
        print(hint4, end='                            ')
    elif g == 0:
        jk = True
        break
    if g > 2:
        print('Guesses Left: ' + str(g), end='                         ')
    else:
        print('\u001b[31mGuesses Left: ' + str(g) + '\u001b[0m', end='                         ')
    if g == 5:
        print('Your guesses so far: None')
    else:
        print('Your guesses so far: ' + list_to_str(guesses_so(guess)))
    guess = input('Enter in your guess: ')
    if guess != str(b) and guess.isdigit():
        g -= 1
    elif guess == str(b) and guess.isdigit():
        break
    else:
        print('\u001b[31mInvalid Response\u001b[0m')
        time.sleep(2)
    print(x)
if jk is True:
    print(x)
    print('\u001b[31mGAME OVER\u001b[0m')
    print('Your final guess: ' + guess + '           The number: ' + str(b))
    time.sleep(3)
    print('Shutting down program.', end='')
    time.sleep(0.8)
    print('.', end='')
    time.sleep(0.8)
    print('.', end='')
    time.sleep(1)
else:
    print(x)
    print('\u001b[32mYAY! YOU GUESSED THE NUMBER!\u001b[0m')
    print('Your guess: ' + guess + '           The number: ' + str(b))
    time.sleep(3)
    print('Shutting down program.', end='')
    time.sleep(0.8)
    print('.', end='')
    time.sleep(0.8)
    print('.', end='')
    time.sleep(1)
