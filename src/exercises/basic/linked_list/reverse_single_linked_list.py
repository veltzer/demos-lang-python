"""
solution
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
        """ get the data of the element """
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
        """ yield all elelemts """
        pointer = self.first_element
        while pointer:
            yield pointer.data
            pointer = pointer.next


def get_reverse(the_list):
    """
    Get a list and return a list with all of it's elements in reverse order
    """
    reverse = SingleLinkedList()
    while not the_list.is_empty():
        reverse.add_head_element(the_list.pop_head_element())
    return reverse


def main():
    """ the main function """
    the_list = SingleLinkedList()
    the_list.add_head_element(3)
    the_list.add_head_element(2)
    the_list.add_head_element(1)
    print("original list follows...")
    for element in the_list.yield_elements():
        print(element)
    reverse = get_reverse(the_list)
    print("reverse list follows...")
    for element in reverse.yield_elements():
        print(element)


main()
