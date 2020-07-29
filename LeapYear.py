import datetime

if datetime.datetime.now().year % 4:
    print('This year is not a leap year')
else:
    print('This year is a leap year')