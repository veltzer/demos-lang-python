"""
Solution1
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def apply_funcs(funcs: list[Callable[..., Any]], x: int):
    """Apply a list of unary functions on an argument,
    Return the result"""
    return map(lambda f: f(x), funcs)  # noqa: C417  teaching: demonstrating map with a lambda
