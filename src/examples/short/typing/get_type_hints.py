#!/usr/bin/env python

"""
An example of how to extract type hints from a class
"""

from typing import get_type_hints


class Data:
    # a: ClassVar[int] = 0
    def doit(a: float) -> float:
        return a + 1


def func(a: int) -> int:
    return a + 1


import __main__

a = 1  # type: int
print(get_type_hints(__main__))

# print(dir(a))


# print(Data.__dict__)
# print(Data)
for x in get_type_hints(Data.__class__):
    print(x)

for x in get_type_hints(func):
    print(x)
