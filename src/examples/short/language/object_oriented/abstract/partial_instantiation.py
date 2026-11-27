"""
This example shows that instantiating only some of the abstract methods keeps
you abstract.
"""

import abc


# This is the right way to do it
class A(abc.ABC):
    @abc.abstractmethod
    def method1(self) -> None:
        pass

    @abc.abstractmethod
    def method2(self) -> None:
        pass


class B(A):
    def method1(self) -> None:
        pass


class C(B):
    def method2(self) -> None:
        pass


try:
    a = A()  # pyrefly: ignore[bad-instantiation]  teaching: abstract classes cannot be instantiated
    assert isinstance(a, A)
except TypeError as e:
    print(f"yes, got exception [{e!s}]...")

try:
    b = B()  # pyrefly: ignore[bad-instantiation]  teaching: abstract classes cannot be instantiated
    assert isinstance(b, B)
except TypeError as e:
    print(f"yes, got exception [{e!s}]...")

c = C()
assert isinstance(c, C)
print("yes, managed to instantiated C")
