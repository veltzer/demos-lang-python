"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

References:
- http://stackoverflow.com/questions/17784849/
in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""

import inspect
import sys


class NoTraceBackWithLineNumber(Exception):
    def __init__(self, msg):
        try:
            ln = sys.exc_info()[-1].tb_lineno
        except AttributeError:
            ln = inspect.currentframe().f_back.f_lineno
        self.args = "{0.__name__} (line {1}): {2}".format(type(self), ln, msg),
        sys.exit(self)


class MyNewError(NoTraceBackWithLineNumber):
    pass


raise MyNewError("Now TraceBack Is Gone")
