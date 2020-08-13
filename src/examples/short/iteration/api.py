"""
This example shows how to use the iterator API.

The API is made of 3 things:
- the 'iter' function to get a new iterator from an iterable.
- the 'next' function to get the new data from an iterator.
- the 'StopIteration' exception which is thrown when there is not
more data be had.
"""

from typing import Iterable


# the following two functions are the same:
def print_all_values_api(i: Iterable):
    iterator = iter(r)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


def print_all_values_loop(i: Iterable):
    for x in i:
        print(x)


r = range(10)
print_all_values_api(r)
print_all_values_loop(r)
