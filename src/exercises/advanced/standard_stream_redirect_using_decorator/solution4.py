"""
solution4.py
"""

import sys
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def with_output_to_outfile(filename: str):
    def creator(f: Callable[..., Any]):
        def decorated_f(*args: Any, **kw: Any):
            old_stdout = sys.stdout
            with open(filename, "a") as new_stdout:
                sys.stdout = new_stdout
                try:
                    return f(*args, **kw)
                finally:
                    sys.stdout = old_stdout
        return decorated_f
    return creator


@with_output_to_outfile(filename="/tmp/foo.txt")
def hello(name: str) -> None:
    print(f"Hello, {name}!")


def main() -> None:
    print("You should not see Fred or Barney on your screen")
    hello("Fred")
    hello("Barney")
    print("You should now see this")


if __name__ == "__main__":
    main()
