"""
This example demostrates that you can throw exceptions
in the middle of python "constructors" (which are
actually initializers).

The explanation is that in python the "__init__" in not
really a constructor but rather a standard method to do
post construction initialization. As such it does not
have any isseu with throwing exceptions or calling methods
that may throw exceptions.
"""


class A:
    def __init__(self):
        raise ValueError("this is my error")


try:
    a = A()
except ValueError as e:
    print(f"yes, got the exception [{e}]")
