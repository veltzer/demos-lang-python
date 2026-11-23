"""
This example shows how to get out of a constructor early.
This is done via "return None" or simply "return" (which is the same).

Notice that you cannot return anything but None. The final value
which is returned to the caller of the constructor is "self" and
that is returned by python, not by your code.

If you do not return None from the constructor you will get the
following error: __init__() should return None

If you want a constructor to return something else than an instance
of the class then you can override the __new__ method. But that
is a different story.
"""

from __future__ import annotations


class Book:
    # noinspection PyReturnFromInit,PyTypeChecker
    # pylint: disable=return-in-init
    def __init__(self, price) -> Book:
        self.__price = price
        # return None
        # noinspection PyTypeChecker
        return 7  # noqa: PLE0101  teaching: __init__ must not return a value  # pyrefly: ignore[bad-return]
        # return

    def set_price(self, val):
        self.__price = val

    def get_price(self):
        return self.__price

    def print_me(self):
        print("print_me: price is", self.__price)


try:
    b = Book(50)
    print(b)
    b.set_price(60)
    print(type(b))
    print(dir(b))
    b.print_me()
except TypeError:
    print("yes, got an exception")
