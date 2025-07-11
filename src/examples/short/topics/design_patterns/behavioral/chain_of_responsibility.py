"""
*What is this pattern about?

The Chain of responsibility is an object oriented version of the
`if ... elif ... elif ... else ...` idiom, with the
benefit that the condition–action blocks can be dynamically rearranged
and reconfigured at runtime.

This pattern aims to decouple the senders of a request from its
receivers by allowing request to move through chained
receivers until it is handled.

Request receiver in simple form keeps a reference to a single successor.
As a variation some receivers may be capable of sending requests out
in several directions, forming a `tree of responsibility`.

*TL;DR
Allow a request to pass down a chain of receivers until it is handled.
"""

from abc import ABC, abstractmethod
from typing import Self
from contextlib import redirect_stdout
import io


class Handler(ABC):
    def __init__(self, successor: Self | None = None):
        self.successor = successor

    def handle(self, request: int) -> None:
        """
        Handle request and stop.
        If cant - call next handler in chain.

        As an alternative you might even in case of success
        call the next handler.
        """
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def check_range(self, request: int) -> bool | None:
        """Compare passed value to predefined interval"""


class ConcreteHandler0(Handler):
    """
    Each handler can be different.
    Be simple and static...
    """
    def check_range(self, request: int) -> bool | None:
        if 0 <= request < 10:
            print(f"request {request} handled in handler 0")
            return True
        return None


class ConcreteHandler1(Handler):
    """... With its own internal state"""

    start, end = 10, 20

    def check_range(self, request: int) -> bool | None:
        if self.start <= request < self.end:
            print(f"request {request} handled in handler 1")
            return True
        return None


class ConcreteHandler2(Handler):
    """... With helper methods."""

    def check_range(self, request: int) -> bool | None:
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f"request {request} handled in handler 2")
            return True
        return None

    @staticmethod
    def get_interval_from_db() -> tuple[int, int]:
        return (20, 30)


class FallbackHandler(Handler):
    def check_range(self, request: int) -> bool | None:
        print(f"end of chain, no handler for {request}")
        return False


CORRECT_OUTPUT = """\
request 2 handled in handler 0
request 5 handled in handler 0
request 14 handled in handler 1
request 22 handled in handler 2
request 18 handled in handler 1
request 3 handled in handler 0
end of chain, no handler for 35
request 27 handled in handler 2
request 20 handled in handler 2
"""


def main():
    h0 = ConcreteHandler0()
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2(FallbackHandler())
    h0.successor = h1
    h1.successor = h2
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    with redirect_stdout(io.StringIO()) as output:
        for request in requests:
            h0.handle(request)
    assert output.getvalue() == CORRECT_OUTPUT


if __name__ == "__main__":
    main()
