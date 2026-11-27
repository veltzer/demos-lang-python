"""
this is a function accepting a list of unary functions and an argument
the function returns a list where each element is the application of the
relevant unary function on the single argument
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def map_like(func_list: list[Callable[..., Any]], arg: int):
    return [func(arg) for func in func_list]


def square(x: int):
    return x * x


def triple(x: int):
    return x * 3


def plusone(x: int):
    return x + 1


print(map_like([square, triple, plusone], 7))
