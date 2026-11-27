"""
A basic python functional "reduce" example
"""

import functools


def add(x: int, y: int):
    return x + y


print(functools.reduce(add, range(100)))
