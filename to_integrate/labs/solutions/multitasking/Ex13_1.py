#! /usr/bin/python

import subprocess
import os
import sys

#(a)
proc = subprocess.run([sys.executable, 'client.py', 'words']) 
print ('Child exited with', proc.returncode)

#(b)
proc = subprocess.run([sys.executable, 'client.py', 'words'],
             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.stderr != None:
    print('error:', proc.stderr.decode())
    
print('output:', proc.stdout.decode())
