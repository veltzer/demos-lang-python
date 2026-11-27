"""
solution2.py
"""

import functools
import os
import sys
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def with_output_to(fname: str):
    """Make decorator to run with stdout redirected to fname.

    The file is opened for appending each time f will be called and
    closed when it returns.
    """

    def decorator(f: Callable[..., Any]):
        @functools.wraps(f)
        def decorated_f(*args: Any, **kw: Any):
            old_stdout = sys.stdout
            with open(fname, "a") as new_stdout:
                sys.stdout = new_stdout
                try:
                    return f(*args, **kw)
                finally:
                    sys.stdout = old_stdout

        return decorated_f

    return decorator


@with_output_to("/tmp/out2.txt")
def hello(name: str) -> None:
    print(f"Hello, {name}!")


def main() -> None:
    # Running this will destroy "/tmp/out2.txt"!
    # make sure file is empty
    with open("/tmp/out2.txt", "w"):
        pass
    # test
    print("This should output nothing:")
    hello("Fred")
    hello("Barney")
    print("The file now contains this:")
    with open("/tmp/out2.txt") as f:
        print(f.read())
    # clean up
    os.remove("/tmp/out2.txt")


main()
