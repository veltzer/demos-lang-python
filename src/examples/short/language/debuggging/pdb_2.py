"""
This is an example of debugging python with pdb.
"""

import pdb  # noqa: T100

# pylint: disable=forgotten-debug-statement
pdb.set_trace()  # noqa: T100


def calc():
    i = 0
    current_sum = 0
    while True:
        current_sum += i
        i += 1


calc()
