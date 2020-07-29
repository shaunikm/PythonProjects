import time
import sys


type_str = 'The Ansi escape codes let you set the color of the text-background the same way it lets you set the color of the foregrond.\n'


sys.stdout.write('\r' + format('This is a typing game/test. It will test how accurately and fast you type.'))
time.sleep(5)
sys.stdout.flush()
sys.stdout.write('\r' + 'Once the game shows you the paragraph, a timer will count down from 3 seconds. Get ready!')
time.sleep(5)
sys.stdout.flush()
sys.stdout.write('\r')
#print(x)

sys.stdout.write('\r' + format(type_str))
for i in range(1, 4):
    sys.stdout.write('\r' + str(i))
    time.sleep(1)
    sys.stdout.flush()

sys.stdout.flush()
sys.stdout.write('\r' + format(''))

kl = time.time()
user_ = sys.stdout.write('\r' + format(input('Type now!\n\u001b[1000D')))
kp = time.time()
sys.stdout.flush()
sys.stdout.write('\r' + format(''))
sys.stdout.write('\r' + 'Processing')
sys.stdout.flush()
time.sleep(0.8)
sys.stdout.write('\rProcessing.')
sys.stdout.flush()
time.sleep(0.8)
sys.stdout.write('\rProcessing..')
sys.stdout.flush()
time.sleep(0.8)
sys.stdout.write('\rProcessing...')
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\r')
timel = 'Time Taken: ' + str(round(kp - kl)) + ' seconds'
sys.stdout.write('\r' + format(timel))