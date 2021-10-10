"""
solution
"""


import random


class Node:
    """
    This is a single element of the singly linked list
    """

    def __init__(self, data, next_element):
        """ constructor """
        self.data = data
        self.next = next_element

    def get_data(self):
        """ get the data from the node """
        return self.data

    def get_next(self):
        """ get the next element """
        return self.next


class SingleLinkedList:
    """
    This is the list implementation
    """

    def __init__(self):
        """ constructor """
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

    def add_sorted(self, data):
        """ add an element to a sorted list """
        prev = None
        pointer = self.first_element
        while pointer is not None and pointer.data < data:
            prev = pointer
            pointer = pointer.next
        node = Node(data, pointer)
        if prev is not None:
            prev.next = node
        else:
            self.first_element = node


def main():
    """ the main function """
    the_list = SingleLinkedList()
    for _ in range(50):
        the_list.add_sorted(random.randint(0, 100))
    for element in the_list.yield_elements():
        print(f"{element} ", end="")


main()
