"""
Demos of how to create a context manager that
that hides prints
"""

import os
import sys
from typing import TYPE_CHECKING, Self, TextIO

if TYPE_CHECKING:
    from types import TracebackType


class SuppressPrint:
    def __init__(self) -> None:
        self._original_stdout: TextIO = sys.stdout
    def __enter__(self) -> Self:
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        sys.stdout.close()
        sys.stdout = self._original_stdout

# Usage
print("This shows")
with SuppressPrint():
    print("This is hidden")
    print("So is this")
print("This shows again")
