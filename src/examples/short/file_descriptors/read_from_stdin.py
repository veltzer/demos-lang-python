"""
This is an example of how to read from a file descriptor (not a file).
"""

import os

for line in os.fdopen(0):
    print(line, end='')
