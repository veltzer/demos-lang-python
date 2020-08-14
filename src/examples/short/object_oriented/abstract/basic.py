"""
This is an example of how to make an abstract class in python

Notes:
- As can be seen from the example a class which only hooks
to the __metaclass__ of abc.ABCMeta CAN BE INSTANTIATED.
- only if the class has at least one abstract method then
it cannot be instantiated (second example).
- in python2 the syntax for this was different:
    class A:
        __metaclass__ = abc.ABCMeta

References:
- https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
"""

import abc


class A(metaclass=abc.ABCMeta):
    pass


a = A()
assert isinstance(a, A)


class B(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def foo(self):
        pass


class C(B):
    def foo(self):
        pass


try:
    b = B()
except TypeError as e:
    print('yes, got exception [{0}]...'.format(str(e)))
c = C()
assert issubclass(C, B)
assert isinstance(c, C)
