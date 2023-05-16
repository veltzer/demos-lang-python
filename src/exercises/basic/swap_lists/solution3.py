"""
solution
"""


def swap_lists(list1, list2):
    """ swap elements in lists """
    # pylint: disable=consider-using-enumerate
    for i in range(len(list1)):
        list1[i], list2[i] = list2[i], list1[i]


def main():
    """ main function """
    list1 = ["a", "b", "c"]
    list2 = [7, 8, 9]
    swap_lists(list1, list2)
    print(list1, list2)


main()
