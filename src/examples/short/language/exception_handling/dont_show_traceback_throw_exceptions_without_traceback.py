"""
This example explores how to inhibit python from printing the stack trace when
exiting from an exception.

References:
- http://stackoverflow.com/questions/17784849/
in-python-how-do-i-print-an-error-message-without-printing-a-traceback-and-clos
"""

import inspect
import sys


class NoTraceBackWithLineNumberError(Exception):
    def __init__(self, msg):
        super().__init__()
        traceback = sys.exc_info()[-1]
        if traceback is not None:
            ln = traceback.tb_lineno
        else:
            frame = inspect.currentframe()
            assert frame is not None
            assert frame.f_back is not None
            ln = frame.f_back.f_lineno
        self.args = (f"{type(self).__name__} (line {ln}): {msg}",)
        sys.exit(str(self))


class MyNewError(NoTraceBackWithLineNumberError):
    pass


raise MyNewError("Now TraceBack Is Gone")
