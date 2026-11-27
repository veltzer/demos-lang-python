"""
solution_oo
"""

import sys
from typing import TYPE_CHECKING, TextIO

if TYPE_CHECKING:
    from types import TracebackType


class RedirectManager:

    def __init__(self, filename: str) -> None:
        print("in __init__", file=sys.stderr)
        self.filename = filename
        self.old_output: TextIO = sys.stdout

    def __enter__(self) -> None:
        print("in __enter__", file=sys.stderr)
        self.old_output = sys.stdout
        sys.stdout = open(self.filename, "w")

    def __exit__(self, exception_type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None:
        print("in __exit__", file=sys.stderr)
        sys.stdout.close()
        sys.stdout = self.old_output


print("You should see this on your screen")
with RedirectManager("/tmp/log.txt"):
    print("You really shouldnt see this on your screen")
    raise ValueError("dummy value")
print("You should see this on your screen")
