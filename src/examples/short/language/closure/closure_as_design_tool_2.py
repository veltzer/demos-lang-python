"""
This is an example of information hiding in functions
"""


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable


def make_print_something(s: str) -> Callable[[], None]:
    def inner() -> None:
        print(s)

    return inner


print_hello = make_print_something("hello")
print_goodbye = make_print_something("goodbye")

print_hello()
print_goodbye()
print_hello()
print_goodbye()
print_hello()
print_hello()
