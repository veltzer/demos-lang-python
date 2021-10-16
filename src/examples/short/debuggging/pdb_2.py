"""
This is an example of debugging python with pdb.
"""

import pdb

# pylint: disable=forgotten-debug-statement
pdb.set_trace()


def calc():
    i = 0
    current_sum = 0
    while True:
        current_sum += i
        i += 1


calc()
