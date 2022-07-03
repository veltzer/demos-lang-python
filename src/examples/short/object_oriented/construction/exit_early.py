"""
This example shows how to get out of a constructor early.
This is done via 'return None' or simply 'return' (which is the same).

Notice that you cannot return anything but None. The final value
which is returned to the caller of the constructor is 'self' and
that is returned by python, not by your code.

If you do not return None from the constructor you will get the
following error: __init__() should return None

If you want a constructor to return something else than an instance
of the class then you can override the __new__ method. But that
is a different story.
"""


class Book:
    # noinspection PyReturnFromInit,PyTypeChecker
    # pylint: disable=return-in-init
    def __init__(self, price) -> 'Book':  # type: ignore
        self.__price = price
        # return None
        # noinspection PyTypeChecker
        return 7  # type: ignore
        # return

    def setPrice(self, val):
        self.__price = val

    def getPrice(self):
        return self.__price

    def printMe(self):
        print('printMe: price is', self.__price)


try:
    b = Book(50)
    print(b)
    b.setPrice(60)
    print(type(b))
    print(dir(b))
    b.printMe()
except TypeError:
    print('yes, got an exception')
