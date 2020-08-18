#!/usr/bin/env python3

class Node:
    """
    This is a single element of the doubly linked list
    """
    def __init__(self, data, next, prev):
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
        pass

    def yield_elements_from_tail_to_head(self):
        pass

def example_of_use():
    l = DoubleLinkedList()
    l.add_head_element(3)
    l.add_head_element(2)
    l.add_head_element(1)
    l.add_tail_element(4)
    l.add_tail_element(5)
    l.add_tail_element(6)

    print("starting forward iteration")
    for e in l.yield_elements_from_head_to_tail():
        print(e)

    print("starting backward iteration")
    for e in l.yield_elements_from_tail_to_head():
        print(e)

    print("popping elements")
    l.pop_head_element()
    l.pop_tail_element()

    print("starting forward iteration")
    for e in l.yield_elements_from_head_to_tail():
        print(e)

    print("popping all remaining elements")
    while not l.is_empty():
        l.pop_head_element()

    print("starting forward iteration")
    for e in l.yield_elements_from_head_to_tail():
        print(e)

example_of_use()
