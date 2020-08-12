"""
This example shows how to handle '~' in file names and shell variables
There are two different ways: expanduser and expandvars
As you can see none of those do path expansions
"""

import os

print(os.path.expanduser('~'))
print(os.path.expanduser('~/.viminfo'))
print(os.path.expandvars('USER is $USER'))
print(os.path.expanduser('ls'))
print(os.path.expandvars('ls'))
