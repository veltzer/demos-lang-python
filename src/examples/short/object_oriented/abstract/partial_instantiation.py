"""
This example shows that instantiating only some of the abstract methods keeps
you abstract.
"""

import abc


# This is the right way to do it
class A(abc.ABC):
    @abc.abstractmethod
    def method1(self):
        pass
    @abc.abstractmethod
    def method2(self):
        pass


class B(A):
    def method1(self):
        pass

class C(B):
    def method2(self):
        pass


try:
    # pylint: disable=abstract-class-instantiated
    a = A()  # type: ignore
    assert isinstance(a, A)
except TypeError as e:
    print(f"yes, got exception [{str(e)}]...")

try:
    # pylint: disable=abstract-class-instantiated
    b = B()  # type: ignore
    assert isinstance(b, B)
except TypeError as e:
    print(f"yes, got exception [{str(e)}]...")

c = C()
assert isinstance(c, C)
print("yes, managed to instantiated C")
