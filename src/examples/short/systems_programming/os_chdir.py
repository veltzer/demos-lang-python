"""
This example shows how to use the os chdir command.
Note that an exception is thrown if a directory name which cannot be
changed to is supplied (bad name, access problem and more).
"""

import os

try:
    # a wrong directory on purpose...
    os.chdir('/no_such_folder')
except FileNotFoundError:
    print('yes, got an exception for a bad directory')
os.chdir('/tmp')
os.system('ls')
