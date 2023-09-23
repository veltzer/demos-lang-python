"""
This is an example with a class with an abstract method and the fact that it cannot
be instantiated. It's subclass which does implement the method can be instantiated.
"""

import abc


# This is the right way to do it
class A(abc.ABC):
    @abc.abstractmethod
    def method(self):
        pass


class B(A):
    def method(self):
        pass


try:
    # pylint: disable=abstract-class-instantiated
    a = A()  # type: ignore
    assert isinstance(a, A)
except TypeError as e:
    print(f"yes, got exception [{str(e)}]...")

b = B()
assert isinstance(b, B)
