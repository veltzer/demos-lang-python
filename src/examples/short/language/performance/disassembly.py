"""
Example of disassembling a python function using the "dis" and "inspect" modules.
"""

import dis
import inspect


def add(a: int, b: int):
    if a % 2 == 1:
        a = a - 7
    return a + b


dis.dis(add)
print(inspect.getsourcelines(add))
