"""
solution
"""

from typing import Any


def swap_lists(list1: list[Any], list2: list[Any]) -> None:
    """ swap elements in lists """
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]


def main() -> None:
    """ main function """
    list1 = ["a", "b", "c"]
    list2 = [7, 8, 9]
    swap_lists(list1, list2)
    print(list1, list2)


main()
