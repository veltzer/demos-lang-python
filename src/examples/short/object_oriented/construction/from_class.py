"""
An example of constructing an object from the class when the class is a parameter.

Notes:
- cls() will do everything you want (construct a new objecd and call the initialization
hook '__init__'.
- __new__ enables you to construct an object *without* calling the '__init__' initialization
hook. flexible.
"""


class A:
    def __init__(self):
        print('in A constructor')


def make_something(cls=None):
    t = cls()
    return t


def make_something_2(cls=None):
    t = cls.__new__(cls)
    return t


def make_something_3(cls=None):
    t = cls.__new__(cls)
    t.__init__()
    return t


a = make_something(A)
print(a)
print(type(a))
a = make_something_2(A)
print(a)
print(type(a))
a = make_something_3(A)
print(a)
print(type(a))
