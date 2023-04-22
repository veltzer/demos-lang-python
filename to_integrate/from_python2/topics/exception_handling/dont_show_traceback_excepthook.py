"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

References:
- http://stackoverflow.com/questions/17784849/in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""

import sys


def do_error():
    raise ValueError('core')


def excepthook(_type, value, _traceback):
    print("here")


sys.excepthook = excepthook

do_error()
print("after")
