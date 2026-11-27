"""
solution.py
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def add1(f: Callable[..., Any]):
    def inner(*args: Any, **kw: Any):
        return f(*args, **kw) + 1

    return inner


def make_a_list(f: Callable[..., Any]):
    def inner(*args: Any, **_kw):
        #    return [f(x) for x in args]  # noqa: ERA001  teaching: kept in the comment for the reader
        return [f(x) for x in args]

    return inner


@make_a_list
def square(x: int):
    return x * x


print(square(3, 2, 1))
