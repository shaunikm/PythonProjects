import time
import random

x = 50*'\n'

m = False
j = False
z = random.randint(1, 9999999999999999999999999999999999)
print('This is the key that you will use to play rock, paper, scissors against the computer:')
print('s - scissors')
print('r - rock')
print('p - paper')
attacks = ['Rock', 'Paper', 'Scissors']
time.sleep(6)
error_ = '\u001b[31mInvalid Response\u001b[0m'
lose = '\u001b[31mRound Lost\u001b[0m'
tie = '\u001b[37mTie!\u001b[0m'
win = '\u001b[32mYou Won!!!\u001b[0m'
print(x)
s = 0
sc = 0
print('f - runs the game forever')
print('l - stops game when a person receives a score that you choose')
print('!q - quits program')
print('!help - gives you a list of commands once in a game\n')
mode_ = input('What mode do you want to choose? ')
mode_ = mode_.lower()
mode_ = mode_.strip()
if mode_ == '!q':
    j = False
    m = False
elif mode_ == 'f':
    m = True
elif mode_ == 'l':
    z = int(input('What is the score you want to reach for the game to end? '))
    j = True
else:
    print(error_)
while m is True:
    print(x)
    print('Your score: ', s, '              The computer\'s score: ', sc)
    attack_ = input('Which move do you choose? ')
    computer_attack = random.choice(attacks)
    attack_ = attack_.lower()
    attack_ = attack_.strip()
    if attack_ == '!help':
        print('s - scissors')
        print('r - rock')
        print('p - paper')
        print('!q - quits program')
        print('!ra - reset scores all scores')
        print('!rc - resets the computer\'s score')
        print('!rm - resets your score')
        print('!sm - set your score to a specific number')
        print('!sc - set the computer\'s score to a specific number')
        print('!help - gives you a list of commands')
        time.sleep(7)
    elif attack_ == 's':
        if computer_attack == 'Rock':
            print('Your choice: Scissors   The Computer\'s choice: ' + computer_attack)
            print(lose)
            print(time.sleep(2))
            if s == 0:
                s = 0
            else:
                s -= 1
            sc += 1
        elif computer_attack == 'Scissors':
            print('Your choice: Scissors   The Computer\'s choice: ' + computer_attack)
            print(tie)
            print(time.sleep(2))
        else:
            print('Your choice: Scissors   The Computer\'s choice: ' + computer_attack)
            print(win)
            print(time.sleep(2))
            s += 1
            if sc == 0:
                sc = 0
            else:
                sc -= 1
    elif attack_ == 'r':
        if computer_attack == 'Scissors':
            print('Your choice: Rock   The Computer\'s choice: ' + computer_attack)
            print(win)
            print(time.sleep(2))
            s += 1
            if sc == 0:
                sc = 0
            else:
                sc -= 1
        elif computer_attack == 'Rock':
            print('Your choice: Rock   The Computer\'s choice: ' + computer_attack)
            print(tie)
            print(time.sleep(2))
        else:
            print('Your choice: Rock   The Computer\'s choice: ' + computer_attack)
            print(lose)
            print(time.sleep(2))
            if s == 0:
                s = 0
            else:
                s -= 1
            sc += 1
    elif attack_ == 'p':
        if computer_attack == 'Rock':
            print('Your choice: Paper   The Computer\'s choice: ' + computer_attack)
            print(win)
            print(time.sleep(2))
            s += 1
            if sc == 0:
                sc = 0
            else:
                sc -= 1
        elif computer_attack == 'Paper':
            print('Your choice: Paper   The Computer\'s choice: ' + computer_attack)
            print(tie)
            print(time.sleep(2))
        else:
            print('Your choice: Paper   The Computer\'s choice: ' + computer_attack)
            print(lose)
            print(time.sleep(2))
            if s == 0:
                s = 0
            else:
                s -= 1
            sc += 1
    elif attack_ == '!q':
        break
    elif attack_ == '!ra':
        s = 0
        sc = 0
    elif attack_ == '!rm':
        s = 0
    elif attack_ == '!rc':
        sc = 0
    elif attack_ == '!sc':
        sc_set = input('What do you want to set the computer\'s score to? ')
        if sc_set.isdigit():
            sc = sc_set
        else:
            print('\u001b[31mThe score cannot be a word\u001b[0m')
    elif attack_ == '!sm':
        sm_set = input('What do you want to set your score to? ')
        if sm_set.isdigit():
            s = sm_set
        else:
            print('\u001b[31mThe score cannot be a word\u001b[0m')
    else:
        print(error_)
        time.sleep(2)

while j is True:
    if int(s) == int(z):
        print(x)
        print('\u001b[32mYOU WON AGAINST THE COMPUTER!!!\u001b[0m')
        print('Your score: ', s, '              The computer\'s score: ', sc)
        time.sleep(2)
        break
    elif int(sc) == int(z):
        print(x)
        print('\u001b[31mYou lost against the computer :(\u001b[0m')
        print('Your score: ', s, '              The computer\'s score: ', sc)
        time.sleep(2)
        break
    print(x)
    print('Your score: ', s, '              The computer\'s score: ', sc)
    attack_ = input('Which move do you choose? ')
    computer_attack = random.choice(attacks)
    attack_ = attack_.lower()
    attack_ = attack_.strip()
    if attack_ == '!help':
        print('s - scissors')
        print('r - rock')
        print('p - paper')
        print('!q - quits program')
        print('!ra - reset scores all scores')
        print('!rc - resets the computer\'s score')
        print('!rm - resets your score')
        print('!help - gives you a list of commands')
        time.sleep(7)
    elif attack_ == 's':
        if computer_attack == 'Rock':
            print('Your choice: Scissors   The Computer\'s choice: ' + computer_attack)
            print(lose)
            print(time.sleep(2))
            if s == 0:
                s = 0
            else:
                s -= 1
            sc += 1
        elif computer_attack == 'Scissors':
            print('Your choice: Scissors   The Computer\'s choice: ' + computer_attack)
            print(tie)
            print(time.sleep(2))
        else:
            print('Your choice: Scissors   The Computer\'s choice: ' + computer_attack)
            print(win)
            print(time.sleep(2))
            s += 1
            if sc == 0:
                sc = 0
            else:
                sc -= 1
    elif attack_ == 'r':
        if computer_attack == 'Scissors':
            print('Your choice: Rock   The Computer\'s choice: ' + computer_attack)
            print(win)
            print(time.sleep(2))
            s += 1
            if sc == 0:
                sc = 0
            else:
                sc -= 1
        elif computer_attack == 'Rock':
            print('Your choice: Rock   The Computer\'s choice: ' + computer_attack)
            print(tie)
            print(time.sleep(2))
        else:
            print('Your choice: Rock   The Computer\'s choice: ' + computer_attack)
            print(lose)
            print(time.sleep(2))
            if s == 0:
                s = 0
            else:
                s -= 1
            sc += 1
    elif attack_ == 'p':
        if computer_attack == 'Rock':
            print('Your choice: Paper   The Computer\'s choice: ' + computer_attack)
            print(win)
            print(time.sleep(2))
            s += 1
            if sc == 0:
                sc = 0
            else:
                sc -= 1
        elif computer_attack == 'Paper':
            print('Your choice: Paper   The Computer\'s choice: ' + computer_attack)
            print(tie)
            print(time.sleep(2))
        else:
            print('Your choice: Paper   The Computer\'s choice: ' + computer_attack)
            print(lose)
            print(time.sleep(2))
            if s == 0:
                s = 0
            else:
                s -= 1
            sc += 1
    elif attack_ == '!q':
        break
    elif attack_ == '!ra':
        s = 0
        sc = 0
    elif attack_ == '!rm':
        s = 0
    elif attack_ == '!rc':
        sc = 0
    else:
        print(error_)
        time.sleep(2)


print('Shutting down program.', end='')
time.sleep(0.8)
print('.', end='')
time.sleep(0.8)
print('.', end='')
time.sleep(1)