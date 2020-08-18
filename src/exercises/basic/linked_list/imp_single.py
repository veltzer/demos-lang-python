"""
References:
- https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
"""

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
