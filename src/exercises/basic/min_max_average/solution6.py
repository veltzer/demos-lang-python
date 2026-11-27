"""
Solution6
"""

import functools


def single_min_max_sum(so_far: tuple[int, int, int], y: int) -> tuple[int, int, int]:
    """ the minimum, maximum and sum of the numbers seen so far and one more """
    return min(so_far[0], y), max(so_far[1], y), so_far[2] + y


def min_max_avg(number_list: range):
    first = number_list[0]
    tup = functools.reduce(single_min_max_sum, number_list[1:], (first, first, first))
    return tup[0], tup[1], tup[2] / len(number_list)


print(min_max_avg(range(100000)))
