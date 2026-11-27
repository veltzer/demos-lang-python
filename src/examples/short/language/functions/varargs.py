"""
This example shows how to use varargs in python to do useful work.
In this case, calling a function many times without knowing the function
or the arguments that it is supposed to receive.
"""


from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable



def call_many_times(func: Callable[..., None], times: int, *args: Any, **kwargs: Any) -> None:
    for _ in range(times):
        func(*args, **kwargs)


call_many_times(print, 5, "hello")
