"""
A simple subprocess demo. Create a subprocess and run it. No pipes.
Find the return code of the process.
"""

import subprocess

try:
    subprocess.Popen(['no such process', '--no-such-option'])
except FileNotFoundError:
    print('yes, got error for it')
p = subprocess.Popen(['sleep', '10'])
print("in here, async, isn't it?")
ret = p.wait()
print('ret is', ret)
