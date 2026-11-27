"""
Solution1
"""

import functools


def my_func(x: int, y: int):
    if y % 2 == 0:
        return x - y
    return x + y


def odds_minus_evens(my_list: range):
    result = functools.reduce(my_func, my_list)
    if my_list[0] % 2 == 0:
        result -= 2 * my_list[0]
    return result


print(odds_minus_evens(range(2, 6)))
