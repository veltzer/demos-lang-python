"""
References:
- https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
"""


class Node:
    """
    This is a single element of the singly linked list
    """

    def __init__(self, data, next_element):
        """ constructor """
        self.data = data
        self.next = next_element

    def get_data(self):
        """ get the data of the node """
        return self.data

    def get_next(self):
        """ get the next element """
        return self.next


class SingleLinkedList:
    """
    This is the list implementation
    """

    def __init__(self):
        self.first_element = None

    def is_empty(self):
        """ is the list empty """
        return self.first_element is None

    def add_head_element(self, data):
        """ add element at the head """
        node = Node(data, self.first_element)
        self.first_element = node

    def pop_head_element(self):
        """ pop element from the head """
        if self.first_element is None:
            raise ValueError("There are no elements to pop")
        rest = self.first_element.data
        self.first_element = self.first_element.next
        return rest

    def yield_elements(self):
        """ yield all elements """
        pointer = self.first_element
        while pointer:
            yield pointer.data
            pointer = pointer.next


def example_of_use():
    """ example of how to use the API """
    the_list = SingleLinkedList()
    the_list.add_head_element(3)
    the_list.add_head_element(2)
    the_list.add_head_element(1)
    print("starting iteration")
    for element in the_list.yield_elements():
        print(element)
    print("ending iteration")
    print(the_list.pop_head_element())
    print(the_list.pop_head_element())


example_of_use()
