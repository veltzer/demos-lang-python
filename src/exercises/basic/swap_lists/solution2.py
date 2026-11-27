"""
solution
"""

from typing import Any


def swap_lists(list1: list[Any], list2: list[Any]) -> None:
    """ swap two lists """
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]
