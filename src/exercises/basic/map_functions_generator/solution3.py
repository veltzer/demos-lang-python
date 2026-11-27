"""
this is a function accepting a list of unary functions and an argument
the function returns a list where each element is the application of the
relevant unary function on the single argument
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def map_like(func_list: list[Callable[..., Any]], *extra: Any, **named_extra: Any):
    return [func(*extra, **named_extra) for func in func_list]


def add(x: int, y: int, _correction_factor: int = 7):
    return x + y


def mul(x: int, y: int, correction_factor: int = 7):
    return x * y - correction_factor


def sub(x: int, y: int, _correction_factor: int = 7):
    return x - y


print(map_like([add, mul, sub], 7, 3, correction_factor=2))
