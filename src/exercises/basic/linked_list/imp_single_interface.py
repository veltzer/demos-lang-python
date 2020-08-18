class Node:
    """
    This is a single element of the singly linked list
    """
    def __init__(self, _data, _next_element):
        pass


class SingleLinkedList:
    """
    This is the list implementation
    """
    def __init__(self):
        pass

    def is_empty(self):
        pass

    def add_head_element(self, data):
        pass

    def pop_head_element(self):
        pass

    def yield_elements(self):
        yield self


def example_of_use():
    test_list = SingleLinkedList()
    test_list.add_head_element(3)
    test_list.add_head_element(2)
    test_list.add_head_element(1)
    print("starting iteration")
    for e in test_list.yield_elements():
        print(e)
    print("ending iteration")
    print(test_list.pop_head_element())
    print(test_list.pop_head_element())


example_of_use()
