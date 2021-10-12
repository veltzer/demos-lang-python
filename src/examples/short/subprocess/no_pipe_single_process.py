"""
A simple subprocess demo. Create a subprocess and run it. No pipes.
Find the return code of the process.
"""

import subprocess

try:
    with subprocess.Popen(['no such process', '--no-such-option']):
        pass
except FileNotFoundError:
    print('yes, got error for it')
with subprocess.Popen(['sleep', '10']) as p:
    print("in here, async, isn't it?")
    ret = p.wait()
    print(f"ret is {ret}")
