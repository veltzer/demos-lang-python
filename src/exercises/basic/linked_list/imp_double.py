class Node:
    """
    This is a single element of the doubly linked list
    """

    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    """
    This is the list implementation
    """

    def __init__(self):
        self.first_element = None
        self.last_element = None

    def is_empty(self):
        return self.first_element is None

    def add_head_element(self, data):
        node = Node(data, self.first_element, None)
        self.first_element = node
        if self.last_element is None:
            self.last_element = node
        if node.next is not None:
            node.next.prev = node

    def add_tail_element(self, data):
        node = Node(data, None, self.last_element)
        self.last_element = node
        if self.first_element is None:
            self.first_element = node
        if node.prev is not None:
            node.prev.next = node

    def pop_head_element(self):
        if self.first_element is None:
            raise ValueError("There are no elements to pop")
        r = self.first_element.data
        self.first_element = self.first_element.next
        if self.first_element is None:
            self.last_element = None
        else:
            self.first_element.prev = None
        return r

    def pop_tail_element(self):
        if self.last_element is None:
            raise ValueError("There are no elements to pop")
        r = self.last_element.data
        self.last_element = self.last_element.prev
        if self.last_element is None:
            self.first_element = None
        else:
            self.last_element.next = None
        return r

    def yield_elements_from_head_to_tail(self):
        pointer = self.first_element
        while pointer:
            yield pointer.data
            pointer = pointer.next

    def yield_elements_from_tail_to_head(self):
        pointer = self.last_element
        while pointer:
            yield pointer.data
            pointer = pointer.prev


def example_of_use():
    the_list = DoubleLinkedList()
    the_list.add_head_element(3)
    the_list.add_head_element(2)
    the_list.add_head_element(1)
    the_list.add_tail_element(4)
    the_list.add_tail_element(5)
    the_list.add_tail_element(6)

    print("starting forward iteration")
    for element in the_list.yield_elements_from_head_to_tail():
        print(element)

    print("starting backward iteration")
    for element in the_list.yield_elements_from_tail_to_head():
        print(element)

    print("popping elements")
    the_list.pop_head_element()
    the_list.pop_tail_element()

    print("starting forward iteration")
    for element in the_list.yield_elements_from_head_to_tail():
        print(element)

    print("popping all remaining elements")
    while not the_list.is_empty():
        the_list.pop_head_element()

    print("starting forward iteration")
    for element in the_list.yield_elements_from_head_to_tail():
        print(element)


example_of_use()
