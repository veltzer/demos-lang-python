"""
solution
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


def get_reverse(l):
    """
    Get a list and return a list with all of it's elements in reverse order
    """
    l2 = SingleLinkedList()
    while not l.is_empty():
        l2.add_head_element(l.pop_head_element())
    return l2

def main():
    l = SingleLinkedList()
    l.add_head_element(3)
    l.add_head_element(2)
    l.add_head_element(1)
    print("original list follows...")
    for d in l.yield_elements():
        print(d)
    l2 = get_reverse(l)
    print("reverse list follows...")
    for d in l2.yield_elements():
        print(d)

main()
