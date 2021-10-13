"""
This example shows how to catch all exceptions, and exit the software in any case.
"""

import sys


def excepthook(_type, value, _traceback):
    # this loop will drill to the core of the problem
    # use only if this is what you want to show...
    # traceback.print_exception(value=value, tb=_traceback, etype=_type)
    while value.__cause__:
        value = value.__cause__
    print("An exception was throw... Refusing to continue...")
    sys.exit(1)


sys.excepthook = excepthook

# simulate a piece of bad code which "swallows" exceptions...
# noinspection PyBroadException
try:
    raise ValueError('core')
except Exception:
    print("haha, got the exception and continuing anyway...")
print("after")

raise ValueError('core')
