"""
This is an example of how to call a class method directly from a reference to the method.
"""

from types import MethodType


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
        MethodType(cls.ref[0], Book)()


# this ref is a bound method, and so can be called
ref_to_method = Book.increment_num
ref_to_method()

# this ref is also bound and so can be called
ref_to_method = Book.ref_full
ref_to_method()

# this ref is an unbloud method, and so cannot be called
ref_to_method = Book.ref[0]
try:
    ref_to_method()
except TypeError as e:
    print(e)
# this is how we bind the method back to the class
MethodType(ref_to_method.__func__, Book)()
