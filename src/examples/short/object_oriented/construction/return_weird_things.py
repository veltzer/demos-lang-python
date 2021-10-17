"""
Trying to return weird things from the constructor

Conclusions:
- you can only return None or nothing (which is None)
from a import constructor.
- this helps you to get out early if you don't want to
execute the rest of the constructor code.
- you cannot return 'self' since the __init__ method is
not really a constructor in object oriented terminology
but rather an initializer function. The object on which
it works is already alive and well and is already determined
and the initializer function has no say in that matter.
That is why it's return value is uninteresting (it is not
even returned to the programmer).
"""


class A:
    # noinspection PyReturnFromInit
    # pylint: disable=return-in-init
    def __init__(self):
        return 0


class B:
    # noinspection PyReturnFromInit
    # pylint: disable=return-in-init
    def __init__(self):
        return None


class C:
    # noinspection PyReturnFromInit
    # pylint: disable=return-in-init
    def __init__(self):
        return self


class D:
    # noinspection PyReturnFromInit
    def __init__(self):
        return


try:
    a = A()
except TypeError as e:
    print(f"yes, got the exception [{e}]")
b = B()
try:
    c = C()
except TypeError as e:
    print(f"yes, got the exception [{e}]")
d = D()
