#this function helps 'unlock and lock' dictionaries in python
#you would need to enter a boolean value for the lock and unlock functions

#the class that holds all the commands
class dict_control:
    def __init__(self, d):
        self.d = d
        self.b = True
        self.j = d

    def unlock(self):
        self.b = True

    def lock(self):
        self.b = False
        self.d = {}

    def access(self):
        if not self.b:
            return '\u001b[31mAccess Denied\u001b[0m'
        else:
            self.d = self.j
            return self.d


    def stat(self):
       if not self.b:
           return 'LOCKED'
       else:
           return 'UNLOCKED'

#main/test code
if __name__ == '__main__':
    exDictionary = {
        'john': 'fluffy',
        'jan' : 'greg'
        }
    dictionary = dict_control(exDictionary)

    dictionary.lock()
    print(dictionary.access())
    print(dictionary.stat())
    dictionary.unlock()
    print(dictionary.access())
    print(dictionary.stat())
    if dictionary.stat() == 'LOCKED':
        print('False')
    else:
        print('True')