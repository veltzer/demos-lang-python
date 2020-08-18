#!/usr/bin/env python3

class Node:
    """
    This is a single element of the singly linked list
    """
    def __init__(self, data, next):
        self.data = data
        self.next = next


class SingleLinkedList:
    """
    This is the list implementation
    """
    def __init__(self):
        self.first_element = None

    def is_empty(self):
        return self.first_element is None

    def add_head_element(self, data):
        node = Node(data, self.first_element)
        self.first_element = node

    def pop_head_element(self):
        if self.first_element is None:
            raise ValueError("There are no elements to pop")
        r = self.first_element.data
        self.first_element = self.first_element.next
        return r

    def yield_elements(self):
        pointer = self.first_element
        while pointer:
            yield pointer.data
            pointer = pointer.next

    def add_sorted(self, data):
        prev = None
        pointer = self.first_element
        while pointer is not None and pointer.data<data:
            prev = pointer
            pointer = pointer.next
        node = Node(data, pointer)
        if prev is not None:
            prev.next = node
        else:
            self.first_element = node


def reverse(l):
    r = SingleLinkedList()
    while not l.is_empty():
        r.add_head_element(l.pop_head_element())
    return r

def merge(l1, l2):
    l = SingleLinkedList()
    pointer1 = l1.first_element
    pointer2 = l2.first_element
    while pointer1 is not None and pointer2 is not None:
        if pointer1.data < pointer2.data:
            l.add_head_element(pointer1.data)
            pointer1 = pointer1.next
        else:
            l.add_head_element(pointer2.data)
            pointer2 = pointer2.next
    while pointer1 is not None:
            l.add_head_element(pointer1.data)
            pointer1 = pointer1.next
    while pointer2 is not None:
            l.add_head_element(pointer2.data)
            pointer2 = pointer2.next
    return reverse(l)

def main():
    l1 = SingleLinkedList()
    import random
    for i in range(10):
        l1.add_sorted(random.randint(0, 100))
    print("first list follows...")
    for d in l1.yield_elements():
        print(f"{d} ", end="")
    print()
    l2 = SingleLinkedList()
    for i in range(10):
        l2.add_sorted(random.randint(0, 100))
    print("second list follows...")
    for d in l2.yield_elements():
        print(f"{d} ", end="")
    print()
    l = merge(l1, l2)
    print("merged list follows...")
    for d in l.yield_elements():
        print(f"{d} ", end="")
    print()

main()
