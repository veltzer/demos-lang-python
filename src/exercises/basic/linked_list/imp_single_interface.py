#!/usr/bin/env python3

class Node:
    """
    This is a single element of the singly linked list
    """
    def __init__(self, data, next):
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
        pass

def example_of_use():
    l = SingleLinkedList()
    l.add_head_element(3)
    l.add_head_element(2)
    l.add_head_element(1)
    print("starting iteration")
    for e in l.yield_elements():
        print(e)
    print("ending iteration")
    print(l.pop_head_element())
    print(l.pop_head_element())

example_of_use()
