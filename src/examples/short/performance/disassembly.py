"""
Example of disassembling a python function using the "dis" and "inspect" modules.
"""

import dis
import inspect


def add(a, b):
    return a + b


dis.dis(add)
print(inspect.getsourcelines(add))
