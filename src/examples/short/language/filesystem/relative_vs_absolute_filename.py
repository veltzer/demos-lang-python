"""
This example shows how to know, in python, whether the file name
that you get is realtive or absolute
"""

import os.path
import sys

for line in sys.stdin:
    # remove white space
    line = line.rstrip()
    if os.path.isabs(line):
        print("absolute")
    else:
        print("relative", os.path.abspath(line))
