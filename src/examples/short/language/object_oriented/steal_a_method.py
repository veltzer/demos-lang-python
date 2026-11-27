"""
Example of stealing a method from another object
"""

from typing import Any


class Book:
    def __init__(self, price: int) -> None:
        """ initializer """
        self.price = price

    def print_me(self) -> None:
        print(f"price is {self.price}")

    def set_price(self, price: int) -> None:
        self.price = price


print("Lets show how we use our object")
b = Book(50)
b.print_me()

print("apply method without object")
m = b.set_price
print(type(m))
m(55)
b.print_me()


def my_func(self: Any) -> None:
    print(f"in myfunc {self.price}")


# when running a function it will not pass the object it is attached to as "self"
# and so we would not have a "self"
try:
    b.new_method_1 = my_func  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time
    print(type(b.new_method_1))  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time
    # noinspection PyArgumentList
    b.new_method_1()  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time
except TypeError:
    print("all is well, got exception")

# You can, however, use it if you pass "self" yourself...
b.new_method_2 = my_func  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time
print(type(b.new_method_2))  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time
b.new_method_2(b)  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time

# Another way is to tie the function directly to the class
# Its type is still a "function" but now you can call it from
# every instance.
Book.new_method_3 = my_func
print(type(Book.new_method_3))  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time
b.new_method_3()  # pyrefly: ignore[missing-attribute]  teaching: the example attaches methods to an instance or class at run time

# who about plugging in a method which already exists in the instance?
# The problem with this is that we still need to pass "self" our selves.
b2 = Book(60)
b2.print_me = my_func  # pyrefly: ignore[bad-assignment, method-assign]  teaching: a function stored over a method does not bind self
b2.print_me(b2)  # pyrefly: ignore[bad-argument-count]  teaching: self must be passed by hand to a function stored on the instance

# Replacing methods at the class level works...
Book.print_me = my_func  # pyrefly: ignore[method-assign]  teaching: the example replaces a method at run time
b.print_me()

# lets see if we can make it a real method
# TBD
# print(dir(type(Book.set_price)))  # noqa: ERA001  teaching: kept in the comment for the reader
# print(dir(type(Book.print_me)))  # noqa: ERA001  teaching: kept in the comment for the reader
# Book.more = method(myfunc)  # noqa: ERA001  teaching: kept in the comment for the reader
# print(type(Book.more))  # noqa: ERA001  teaching: kept in the comment for the reader
