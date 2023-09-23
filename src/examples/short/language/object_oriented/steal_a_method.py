# type: ignore
"""
Example of stealing a method from another object
"""


class Book:
    def __init__(self, price):
        """ initializer """
        self.price = price

    def print_me(self):
        print(f"price is {self.price}")

    def set_price(self, price):
        self.price = price


print("Lets show how we use our object")
b = Book(50)
# pylint: disable=no-value-for-parameter
b.print_me()

print("apply method without object")
m = b.set_price
print(type(m))
m(55)
b.print_me()


def my_func(self):
    print(f"in myfunc {self.price}")


# when running a function it will not pass the object it is attached to as "self"
# and so we would not have a "self"
try:
    # pylint: disable=attribute-defined-outside-init
    b.new_method_1 = my_func
    print(type(b.new_method_1))
    # noinspection PyArgumentList
    b.new_method_1()
except TypeError:
    print("all is well, got exception")

# You can, however, use it if you pass "self" yourself...
# pylint: disable=attribute-defined-outside-init
b.new_method_2 = my_func
print(type(b.new_method_2))
b.new_method_2(b)

# Another way is to tie the function directly to the class
# Its type is still a "function" but now you can call it from
# every instance.
Book.new_method_3 = my_func
print(type(Book.new_method_3))
b.new_method_3()

# who about plugging in a method which already exists in the instance?
# The problem with this is that we still need to pass "self" our selves.
b2 = Book(60)
b2.print_me = my_func
b2.print_me(b2)

# Replacing methods at the class level works...
Book.print_me = my_func
b.print_me()

# lets see if we can make it a real method
# TBD
# print(dir(type(Book.set_price)))
# print(dir(type(Book.print_me)))
# Book.more = method(myfunc)
# print(type(Book.more))
