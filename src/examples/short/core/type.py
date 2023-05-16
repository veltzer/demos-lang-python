"""
This example demostrates types in python and the use of the "type" function.
You can see that there is a difference between an object inheriting from object
and one which does not. See the more advanced oo examples to explain this
difference in detail.
"""

import math


def my_func():
    pass


class A:
    def __init__(self, val):
        self.privar = val


class B:
    def __init__(self, val):
        self.privar = val


my_list = [
    5,
    5.5,
    5 + 6j,
    "this is a string",
    True,
    False,
    None,
    [1, 2, 3],
    {},
    set(),
    (),
    type,
    max,
    math.sin,
    my_func,
    A(6),
    B(6)
]

print(map(type, my_list))
