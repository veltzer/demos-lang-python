"""
this is an example of a context manager whose __enter__
does not return self
"""

from typing import IO, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from types import TracebackType


class FileManager:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file: IO[Any] | None = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file  # Return the file object, not self

    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None:
        if self.file:
            self.file.close()

# Usage - we get the file object directly
with FileManager("test.txt", "w") as f:
    f.write("Hello World")  # f is the file object, not FileManager
    f.write("Another line")
