"""
This is an example of how to create a decorator which can receive
a parameter (n in this case).

Another things about this example is that we decorate "by hand"
without using the `@` python syntax.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def multply_by(func: Callable[..., Any], n: int):
    """
    The thing to understand about this decorator is that it can decorate
    any function because of the use of *arg, **kwargs and the return value
    """
    def inner(*arg: Any, **kwargs: Any):
        return func(*arg, **kwargs) * n
    return inner


def add(a: int, b: int):
    return a + b


def square(x: int):
    return x * x


add = multply_by(add, 5)
print(f"did you know that 2+2={add(2,2)}")
square = multply_by(square, 7)
print(f"did you know that 2*2={square(2)}")
