"""
This context manager suppresses all exceptions
"""

from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from types import TracebackType


class SuppressAll:
    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool:
        # Return True to suppress any exception
        return True

# Usage
with SuppressAll():
    print("This will run")
    raise ValueError("This error will be suppressed")
    print("This won't run because of the exception above")

print("This will run - exception was suppressed")
