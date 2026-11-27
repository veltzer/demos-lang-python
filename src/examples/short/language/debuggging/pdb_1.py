"""
This is an example of how to debug a python application
just run this application and you will enter debug mode
as soon as you start the trace...
"""

import pdb  # noqa: T100  teaching: this file demonstrates the debugger

# This will make you enter debug start right from the start...
# pdb.set_trace()  # noqa: ERA001  teaching: kept in the comment for the reader


def calc():
    i = 0
    current_sum = 0
    while True:
        current_sum += i
        if i == 600:
            pdb.set_trace()  # noqa: T100  teaching: this file demonstrates the debugger
        i += 1


calc()
