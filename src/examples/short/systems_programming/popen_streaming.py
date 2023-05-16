"""
This example shows how to call popen and get the return text.
"""

import os

# mode="r" is the default
pout = os.popen("./demo_process.py")
for line in pout:
    print("line is", line, end="")
