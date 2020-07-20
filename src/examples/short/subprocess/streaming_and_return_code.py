#!/usr/bin/env python

"""
This is an example of how to use the subprocess module for streaming
"""

import subprocess

p = subprocess.Popen(['./demo_process.py'], shell=False,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# do not use p.stdout.readlines() in the next line as it will block...
for line in p.stdout:
    line = line.decode().rstrip()
    print('line is', line)
print('return code is', p.returncode)

# this is another version but which gives you an addition last line of ''
# while p.poll() is None:
#    line=p.stdout.readline().decode().rstrip()
#    print('line is', line)
