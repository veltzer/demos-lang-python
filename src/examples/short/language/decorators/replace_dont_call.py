"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def decor(_func) -> Callable[[], None]:
    def inner() -> None:
        print("goodbye")
    return inner


@decor
def demo_bar() -> None:
    print("hello")


demo_bar()
