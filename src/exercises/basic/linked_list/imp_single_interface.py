"""
interfaces to be implemented
"""


class Node:
    """
    This is a single element of the singly linked list
    """
    def __init__(self, _data, _next_element):
        pass

    def print(self):
        """ print the current object """

    def get_data(self):
        """ get data from the current object """


class SingleLinkedList:
    """
    This is the list implementation
    """
    def __init__(self):
        pass

    def is_empty(self):
        """ is the current element empty """

    def add_head_element(self, data):
        """ add element at the head """

    def pop_head_element(self):
        """ pop the element the head of the list """

    def yield_elements(self):
        """ yield all elements from the list """


def example_of_use():
    """ example of how your object could be used """
    test_list = SingleLinkedList()
    test_list.add_head_element(3)
    test_list.add_head_element(2)
    test_list.add_head_element(1)
    print("starting iteration")
    for element in test_list.yield_elements():
        print(element)
    print("ending iteration")
    print(test_list.pop_head_element())
    print(test_list.pop_head_element())


example_of_use()
