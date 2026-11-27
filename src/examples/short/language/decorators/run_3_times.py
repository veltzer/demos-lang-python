"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""


from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def run_3_times(func: Callable[..., Any]) -> Callable[[], None]:
    def inner() -> None:
        func()
        func()
        func()
    return inner


@run_3_times
def demo_bar() -> None:
    print("hello")


demo_bar()
