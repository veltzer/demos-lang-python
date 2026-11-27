"""
this is an example of how the "map" function in python works
this is a naive implementation. the python implementation is coded
in C and is a lot faster than this one...
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def my_map(func: Callable[..., Any], val_list: range):
    return [func(value) for value in val_list]


def square(x: int):
    return x * x


print(my_map(square, range(2, 8)))
