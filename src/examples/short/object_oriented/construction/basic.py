"""
Examples of constructors in python.
You must accept at least one argument in a constructor in order for it
to count as a constructor. You can also write a 'varargs' constructor.
Errors for not having the right method occur at runtime and not at
compile time. Because python does not have overloading then if you
do decide to write an __init__ method you have to write it well in
order to avoid a runtime error.

Note that in python2.7 you should have inherited from 'object'
this is no longer required in python3.

strictly speaking __init__ in python is not a constructor
but an initializer since __init__ receives 'self' which is already
an object of the required type.

If you don't write an explicit '__init__' initializer for your
class then your class still works. It's just that it's empty.
"""


# class without a constructor
class NoCons:
    pass


class A:
    # wrong! don't do this...
    # noinspection PyMethodParameters
    # pylint: disable=no-method-argument
    def __init__():
        print('in A constructor')


class B:
    def __init__(self):
        print('in B constructor')
        print(type(self))


class C:
    def __init__(self, _arg1, _arg2):
        print('in C constructor')
        print(type(self))


class D:
    def __init__(self, *_args):
        print('in D constructor')
        print(type(self))


class E:
    def __init__(self, *_args, **__kwargs):
        print('in E constructor')
        print(type(self))


n = NoCons()
print(type(n))
try:
    # pylint: disable=too-many-function-args
    a = A()
except TypeError:
    print('oh,no. Cant construct an object. Must pass self')
b = B()
print(type(b))
c = C(2, 3)
print(type(c))
d = D()
print(type(d))
e = E()
print(type(e))
