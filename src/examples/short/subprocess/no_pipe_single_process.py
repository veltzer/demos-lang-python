#!/usr/bin/env python

"""
A simple subprocess demo. Create a subprocess and run it. No pipes.
Find the return code of the process.
"""

import subprocess

try:
    p = subprocess.Popen(['no such process', '--no-such-option'])
except:
    print('yes, got error for it')
p = subprocess.Popen(['sleep', '10'])
print('in here, async, isnt it?')
ret = p.wait()
print('ret is', ret)
