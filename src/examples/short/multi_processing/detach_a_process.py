"""
This is an example of how to detach from a process in pure python

References:
- http://stackoverflow.com/questions/30519366/pythonic-way-to-detach-a-process
"""

import os
import time

if os.fork() == 0:
    for i in range(10):
        time.sleep(1)
        print('im still here {0}...'.format(i))
