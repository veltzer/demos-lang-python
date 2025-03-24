"""
Solution5
"""

import functools


def my_min(x, y):
    if x < y:
        return x
    return y


def my_max(x, y):
    if x < y:
        return y
    return x


def my_sum(x, y):
    return x + y


def min_max_avg(number_list):
    min_value = functools.reduce(my_min, number_list)
    max_value = functools.reduce(my_max, number_list)
    sum_value = functools.reduce(my_sum, number_list)
    return min_value, max_value, sum_value / len(number_list)


print(min_max_avg(range(0, 100)))
