"""
solution
"""


def swap_lists(list1, list2):
    """ swap two lists """
    # pylint: disable=consider-using-enumerate
    for i in range(len(list1)):
        [list1[i], list2[i]] = [list2[i], list1[i]]


def main():
    """ main function """
    list1 = [2, 3, 4]
    list2 = [8, 7, 6]
    swap_lists(list1, list2)
    print(list1)
    print(list2)


main()
