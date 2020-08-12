"""
This is a demo process that others will run.
It will send some data and then exit.
"""

import random
import sys
import time

for x in range(5):
    print(x)
    sys.stdout.flush()
    time.sleep(1)
ret = random.randint(0, 255)
print('going to return', ret)
sys.exit(ret)
