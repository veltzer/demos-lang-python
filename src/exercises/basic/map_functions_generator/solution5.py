"""
Naive version of a solution, just construct a list...
No generators here.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable



def apply_funcs(funcs: list[Callable[[int], int]], x: int):
    """ a different version with an iteration """
    return [f(x) for f in funcs]


print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
