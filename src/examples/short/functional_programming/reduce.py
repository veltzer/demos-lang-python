"""
A basic python functional 'reduce' example
"""

import functools


def add(x, y):
    return x + y


print(functools.reduce(add, range(100)))
