"""
solution
"""


def swap_lists(list1, list2):
    """ swap two lists """
    # pylint: disable=consider-using-enumerate
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]
