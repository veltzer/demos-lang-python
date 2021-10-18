"""
This is an example of different exit strategies for python

A few notes:
- exit(N) exists with no printing of the exception it throws.
- exit(N) returns the right code to the parent process
    (view over the shell with 'echo $?')
- os._exit(N) exists immediately (just like _exit(2)).
"""


import sys

try:
    # os._exit(113)
    # exit(114)
    sys.exit(115)
except SystemExit:
    print("hey,I did not exit")
