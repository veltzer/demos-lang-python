"""
Solution10
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable



def apply_funcs(funcs: list[Callable[[int], int]], x: int):
    return (f(x) for f in funcs)


# this does not work (prints "generator something"...)
print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
# this is the way to get the data out of the generator...
for v in apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5):
    print(v)
