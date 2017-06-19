#!/usr/bin/python3

"""
Example of disassembling a python function using the 'dis' and 'inspect' modules.
"""

import dis
import inspect


def add(a, b):
    return a + b

print(dis.dis(add))
print(inspect.getsourcelines(add))
