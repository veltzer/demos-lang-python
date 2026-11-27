"""
An even better implementation of map as a generator.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def my_map(func: Callable[..., Any], val_list: range):
    for value in val_list:
        yield func(value)


def square(y: int):
    return y * y


for x in my_map(square, range(2, 8)):
    print(x)
