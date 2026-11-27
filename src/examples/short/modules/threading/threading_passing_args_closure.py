"""
This is an example of creating a thread and passing it data via its closure
"""

import threading
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

# this function was written with NO consideratiion of threading...


def func(data: Any) -> None:
    print(data)


# this is a wrapper that creates a function with no argument
# that runs any other function with arguments


def create_func(func_to_run: Callable[..., Any], data: str) -> Callable[[], None]:
    def wrapper() -> None:
        func_to_run(data)

    return wrapper


myfunc = create_func(func, "Hello,World")
t = threading.Thread(target=myfunc)
t.start()
t.join()
