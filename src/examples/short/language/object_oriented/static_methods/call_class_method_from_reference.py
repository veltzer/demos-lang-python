"""
This is an example of how to call a class method directly from a reference to the method.
"""

from types import MethodType
from typing import Any
from collections.abc import Callable


class Book:
    num = 0

    def __init__(self, title):
        self.title = title

    @classmethod
    def increment_num(cls):
        print("in increment_num")
        cls.num += 1
        return cls.num

    ref_full = increment_num
    ref = [increment_num]

    @classmethod
    def call_it(cls):
        # pylint: disable=not-callable
        MethodType(cls.ref[0], Book)()


# this ref is a bound method, and so can be called
ref_to_method = Book.increment_num
ref_to_method()

# this ref is also bound and so can be called
ref_to_method_2: Callable[[type[Book]], Any] = Book.ref_full
ref_to_method_2()  # type: ignore

# this ref is an unbloud method, and so cannot be called
ref_to_method_3: Callable[[type[Book]], Any] = Book.ref[0]
try:
    ref_to_method_3()  # type: ignore
except TypeError as e:
    print(e)
# this is how we bind the method back to the class
# pylint: disable=not-callable
MethodType(ref_to_method_3.__func__, Book)()  # type: ignore
