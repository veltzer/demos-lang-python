"""
An example of how to extract type hints from a class
"""

from typing import get_type_hints

import __main__


class Data:
    # a: ClassVar[int] = 0  # noqa: ERA001  teaching: kept in the comment for the reader
    def doit(self, param: float) -> float:
        return param + 1


def func(param: int) -> int:
    return param + 1


a = 1  # type: int
print(get_type_hints(__main__))

# print(dir(a))  # noqa: ERA001  teaching: kept in the comment for the reader


# print(Data.__dict__)  # noqa: ERA001  teaching: kept in the comment for the reader
# print(Data)  # noqa: ERA001  teaching: kept in the comment for the reader
for x in get_type_hints(Data.__class__):
    print(x)

for x in get_type_hints(func):
    print(x)
