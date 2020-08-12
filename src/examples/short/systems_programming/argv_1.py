"""
This example shows how you can use sys.argv[0] in order to make a 'multi-script'.
This means a script that behaves differently according to the manner in which it
is called. When doing it you can symlink various names to your script and get
diffrent behaviour. An prime example of this (although not in python) is the busybox
toolset for embedded linux systems.
"""

import sys

if sys.argv[0] == './argv_1.py':
    print('Heya. you called ./argv_1.py')
else:
    print('Heya. you called by', sys.argv[0])
