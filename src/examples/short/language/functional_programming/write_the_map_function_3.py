"""
this is an example of implementing the python builtin "map"
function in python.

Obviously you should not use this approach and it is presented
for pedagogic purposes only. Pythons own "map" is written in C
and performs much better.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable



def my_map(f: Callable[[int], int], seq: Iterable[int]) -> list[int]:
    return [f(x) for x in seq]


print(my_map(lambda x: x * x, range(10)))
