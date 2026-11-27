"""
solution
"""


def swap_lists(list1: list[int], list2: list[int]) -> None:
    """ swap two lists """
    for i in range(len(list1)):
        [list1[i], list2[i]] = [list2[i], list1[i]]


def main() -> None:
    """ main function """
    list1 = [2, 3, 4]
    list2 = [8, 7, 6]
    swap_lists(list1, list2)
    print(list1)
    print(list2)


main()
