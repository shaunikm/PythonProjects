import sys
import time

progressVis = {0: '          ', 1: '-         ', 2: '--        ', 3: '---       ', 4: '----      ', 5: '-----     ',
               6: '------    ', 7: '-------   ', 8: '--------  ', 9: '--------- ', 10: '----------'}

size = 20
for i in range(0, size):
    percent = int((float(i + 1) / size) * 10)
    str1 = "\r \r [{0}] {1}/{2} {3}%".format(progressVis[percent],
                                                 i + 1, size,
                                                 ((i + 1) * 100 / size))
    sys.stdout.write(str1)
    sys.stdout.flush()
    time.sleep(0.1)