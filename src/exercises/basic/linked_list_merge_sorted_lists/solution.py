"""
solution
"""

import random


class Node:
    """
    This is a single element of the singly linked list
    """

    def __init__(self, data, next_data):
        """ constructor """
        self.data = data
        self.next = next_data

    def print(self):
        """ print the current object """
        print(self.data, self.next)

    def get_data(self):
        """ get the data of the current object """
        return self.data


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
        """ pop the element at the head """
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
        """ add element to a sorted list """
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


def reverse(a_list):
    """ reverse a list """
    rev = SingleLinkedList()
    while not a_list.is_empty():
        rev.add_head_element(a_list.pop_head_element())
    return rev


def merge(list1, list2):
    """ merge two lists """
    merged = SingleLinkedList()
    pointer1 = list1.first_element
    pointer2 = list2.first_element
    while pointer1 is not None and pointer2 is not None:
        if pointer1.data < pointer2.data:
            merged.add_head_element(pointer1.data)
            pointer1 = pointer1.next
        else:
            merged.add_head_element(pointer2.data)
            pointer2 = pointer2.next
    while pointer1 is not None:
        merged.add_head_element(pointer1.data)
        pointer1 = pointer1.next
    while pointer2 is not None:
        merged.add_head_element(pointer2.data)
        pointer2 = pointer2.next
    return reverse(merged)


def main():
    """ the main function """
    list1 = SingleLinkedList()
    for _ in range(10):
        list1.add_sorted(random.randint(0, 100))
    print("first list follows...")
    for element in list1.yield_elements():
        print(f"{element} ", end="")
    print()
    list2 = SingleLinkedList()
    for _ in range(10):
        list2.add_sorted(random.randint(0, 100))
    print("second list follows...")
    for element in list2.yield_elements():
        print(f"{element} ", end="")
    print()
    merged = merge(list1, list2)
    print("merged list follows...")
    for element in merged.yield_elements():
        print(f"{element} ", end="")
    print()


main()
