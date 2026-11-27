"""
Solution6
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable



def apply_funcs(funcs: list[Callable[[int], int]], x: int) -> map[int]:
    """Apply a list of unary functions on an argument,
    Return the result"""
    return map(lambda f: f(x), funcs)  # noqa: C417  teaching: demonstrating map with a lambda


print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
