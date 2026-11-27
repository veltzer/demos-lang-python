"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""

import random
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def sum_10(func: Callable[..., Any]):
    def inner():
        my_sum = 0
        for _ in range(10):
            my_sum += func()
        return my_sum
    return inner


@sum_10
def return_some_number() -> float:
    return random.random()


@sum_10
def return_1() -> int:
    return 1


print(return_some_number())
print(return_1())
