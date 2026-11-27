"""
interfaces to be implemented
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Generator


class Node:
    """
    This is a single element of the singly linked list
    """
    def __init__(self, _data, _next_element) -> None:
        pass

    def print(self) -> None:
        """ print the current object """

    def get_data(self) -> None:
        """ get data from the current object """


class SingleLinkedList:
    """
    This is the list implementation
    """
    def __init__(self) -> None:
        pass

    def is_empty(self) -> None:
        """ is the current element empty """

    def add_head_element(self, data: int) -> None:
        """ add element at the head """

    def pop_head_element(self) -> None:
        """ pop the element the head of the list """

    def yield_elements(self) -> Generator[Any]:
        """ yield all elements from the list """
        yield


def example_of_use() -> None:
    """ example of how your object could be used """
    test_list = SingleLinkedList()
    test_list.add_head_element(3)
    test_list.add_head_element(2)
    test_list.add_head_element(1)
    print("starting iteration")
    for element in test_list.yield_elements():
        print(element)
    print("ending iteration")
    print(test_list.pop_head_element())
    print(test_list.pop_head_element())


example_of_use()
