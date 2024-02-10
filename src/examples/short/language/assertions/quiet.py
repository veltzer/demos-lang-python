"""
This example shows how to create a quiet version of assert in python.
The python "assert" cannot be overloaded as it is not a function but a language keyword.
"""

import sys


def my_assert(cond, msg=None):
    if not cond:
        print(f"Assertion failed message={msg}", file=sys.stderr)
        sys.exit(1)


my_assert(2 + 2 == 5, "math error")
