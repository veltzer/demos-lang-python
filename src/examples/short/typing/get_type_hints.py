"""
An example of how to extract type hints from a class
"""

from typing import get_type_hints

from pyfakeuse import fake_use


class Data:
    # a: ClassVar[int] = 0
    def doit(self, param: float) -> float:
        fake_use(self)
        return param + 1


def func(param: int) -> int:
    return param + 1


# from . import __main__
# pylint: disable=wrong-import-position
import __main__  # noqa: E402

a = 1  # type: int
print(get_type_hints(__main__))

# print(dir(a))


# print(Data.__dict__)
# print(Data)
for x in get_type_hints(Data.__class__):
    print(x)

for x in get_type_hints(func):
    print(x)
