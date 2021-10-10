"""
solution
"""


class Node:
    """
    This is a single element of the doubly linked list
    """

    def __init__(self, _data, _next_element, _prev_element):
        """ constructor """

    def get_data(self):
        """ get data from the node """

    def get_next(self):
        """ get the next element """


class DoubleLinkedList:
    """
    This is the list implementation
    """

    def __init__(self):
        """ constructor """

    def is_empty(self):
        """ is the list empty """

    def add_head_element(self, data):
        """ add element at the head """

    def add_tail_element(self, data):
        """ add element at the tail """

    def pop_head_element(self):
        """ pop element at the head """

    def pop_tail_element(self):
        """ pop element at the tail """

    def yield_elements_head_to_tail(self):
        """ yield elements from head to tail """

    def yield_elements_tail_to_head(self):
        """ yield elements from tail to head """


def example_of_use():
    """ example of how to use the API """
    test_list = DoubleLinkedList()
    test_list.add_head_element(3)
    test_list.add_head_element(2)
    test_list.add_head_element(1)
    test_list.add_tail_element(4)
    test_list.add_tail_element(5)
    test_list.add_tail_element(6)

    print("starting forward iteration")
    for element in test_list.yield_elements_head_to_tail():
        print(element)

    print("starting backward iteration")
    for element in test_list.yield_elements_tail_to_head():
        print(element)

    print("popping elements")
    test_list.pop_head_element()
    test_list.pop_tail_element()

    print("starting forward iteration")
    for element in test_list.yield_elements_head_to_tail():
        print(element)

    print("popping all remaining elements")
    while not test_list.is_empty():
        test_list.pop_head_element()

    print("starting forward iteration")
    for element in test_list.yield_elements_head_to_tail():
        print(element)


example_of_use()
