"""
This is an example of how to pass parameters to a decorator.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def multply_by(n: int):
    def decorator_func(func: Callable[..., Any]):
        def inner(*arg: Any, **kwargs: Any):
            return func(*arg, **kwargs) * n
        return inner
    return decorator_func


@multply_by(n=5)
def add(a: int, b: int):
    return a + b


print(f"did you know that 2+2={add(2,2)}")
