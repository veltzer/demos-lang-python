"""
This is an example of how to make an abstract class in python

Notes:
- As can be seen from the example a class which only hooks
to the __metaclass__ of abc.ABCMeta CAN BE INSTANTIATED.
- only if the class has at least one abstract method then
it cannot be instantiated.
- in python2 the syntax for this was different:
    class A:
        __metaclass__ = abc.ABCMeta

References:
- https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
- https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python
"""

import abc


# This is the right way to do it
class A(abc.ABC):
    @abc.abstractmethod
    def method(self):
        pass


class B(metaclass=abc.ABCMeta):
    pass


class C(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def method(self):
        pass


class D(C):
    def method(self):
        pass


try:
    # pylint: disable=abstract-class-instantiated
    a = A()
    assert isinstance(a, A)
except TypeError as e:
    print(f"yes, got exception [{str(e)}]...")

b = B()
assert isinstance(b, B)

try:
    # pylint: disable=abstract-class-instantiated
    c = C()
    assert issubclass(c, C)
except TypeError as e:
    print(f"yes, got exception [{str(e)}]...")

assert issubclass(D, C)
d = D()
assert isinstance(d, D)
