# noinspection PyPep8
"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

Note that the exception is still throw and the program stopped.

References:
- http://stackoverflow.com/questions/17784849/in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""

import sys


def do_error():
    try:
        raise ValueError('core')
    except Exception as e:
        raise ValueError('outer') from e


def excepthook(_type, value, _traceback):
    # this loop will drill to the core of the problem
    # use only if this is what you want to show...
    # traceback.print_exception(value=value, tb=_traceback, etype=_type)
    while value.__cause__:
        value = value.__cause__
    print(value)


sys.excepthook = excepthook

do_error()
print("after")
