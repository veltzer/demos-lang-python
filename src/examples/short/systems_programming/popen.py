"""
This example shows how to call popen and get the return text.
"""

import os

pout = os.popen('ls -l')
for number, line in enumerate(pout):
    print(number, line, end='')
