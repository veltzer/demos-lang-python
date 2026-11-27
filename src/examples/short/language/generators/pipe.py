"""
Example of generators using generators
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable



def list_input():
    counter = 0
    while True:
        yield counter
        counter += 1
        if counter == 10:
            break


def square_it(input_generator: Callable[[], Iterable[int]]):
    for x in input_generator():
        yield x ** 2


def main() -> None:
    result = [x + 1 for x in square_it(list_input)]
    print(result)


main()
