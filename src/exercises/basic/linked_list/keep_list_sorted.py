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

def main():
    import random
    l = SingleLinkedList()
    for i in range(50):
        l.add_sorted(random.randint(0, 100))
    for d in l.yield_elements():
        print(f"{d} ", end="")

main()
