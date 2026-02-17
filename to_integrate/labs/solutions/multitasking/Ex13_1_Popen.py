#! /usr/bin/python

from subprocess import Popen, PIPE
import sys

#(a)
proc = Popen([sys.executable, 'client.py', 'words']) 
proc.wait()
print ("Child exited with", proc.returncode)

#(b)
proc = Popen([sys.executable, 'client.py', 'words'],
             stdout=PIPE, stderr=PIPE)
(output, error) = proc.communicate()

if error is not None:
    print('error:', error.decode())
    
print('output:', output.decode())


