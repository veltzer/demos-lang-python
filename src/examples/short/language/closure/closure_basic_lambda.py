"""
This is a basic closure example.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable



def make_adder(x: int) -> Callable[[int], int]:
    return lambda y: x + y


add5 = make_adder(5)
add3 = make_adder(3)

print(add5(7))  # 12
print(add5(12))  # 17
print(add3(5))  # 8
print(add3(2))  # 5
