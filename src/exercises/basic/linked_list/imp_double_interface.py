class Node:
    """
    This is a single element of the doubly linked list
    """

    def __init__(self, _data, _next_element, _prev_element):
        pass


class DoubleLinkedList:
    """
    This is the list implementation
    """

    def __init__(self):
        pass

    def is_empty(self):
        pass

    def add_head_element(self, data):
        pass

    def add_tail_element(self, data):
        pass

    def pop_head_element(self):
        pass

    def pop_tail_element(self):
        pass

    def yield_elements_from_head_to_tail(self):
        yield self

    def yield_elements_from_tail_to_head(self):
        yield self


def example_of_use():
    test_list = DoubleLinkedList()
    test_list.add_head_element(3)
    test_list.add_head_element(2)
    test_list.add_head_element(1)
    test_list.add_tail_element(4)
    test_list.add_tail_element(5)
    test_list.add_tail_element(6)

    print("starting forward iteration")
    for e in test_list.yield_elements_from_head_to_tail():
        print(e)

    print("starting backward iteration")
    for e in test_list.yield_elements_from_tail_to_head():
        print(e)

    print("popping elements")
    test_list.pop_head_element()
    test_list.pop_tail_element()

    print("starting forward iteration")
    for e in test_list.yield_elements_from_head_to_tail():
        print(e)

    print("popping all remaining elements")
    while not test_list.is_empty():
        test_list.pop_head_element()

    print("starting forward iteration")
    for e in test_list.yield_elements_from_head_to_tail():
        print(e)


example_of_use()
