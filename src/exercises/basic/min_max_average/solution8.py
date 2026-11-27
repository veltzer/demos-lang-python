"""
Solution8
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def my_min(lst: Sequence[int]):
    cur_min = lst[0]
    for x in lst:
        cur_min = min(cur_min, x)
    return cur_min


def my_max(lst: Sequence[int]):
    cur_max = lst[0]
    for x in lst:
        cur_max = max(cur_max, x)
    return cur_max


def my_sum(lst: Sequence[int]):
    cur_sum = 0
    for x in lst:
        cur_sum += x
    return cur_sum


def min_max_avg(lst: range):
    return my_min(lst), my_max(lst), my_sum(lst) / len(lst)


print(min_max_avg(range(100000)))
