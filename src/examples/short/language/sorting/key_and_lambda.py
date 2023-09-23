"""
This example how to quickly use key and partial to achieve custom sorting.
"""

import operator

# we want to sort according to the second element of the tuple

# long way
mylist = [(1, 7), (2, 5), (0, 0), (3, 8), (1, 8), (2, 8)]


def get_second(t):
    return t[1]


mylist.sort(key=get_second)
print(mylist)

# short way
mylist = [(1, 7), (2, 5), (0, 0), (3, 8), (1, 8), (2, 8)]
mylist.sort(key=lambda t: t[1])
print(mylist)

# using operator
mylist = [(1, 7), (2, 5), (0, 0), (3, 8), (1, 8), (2, 8)]
mylist.sort(key=operator.itemgetter(1))
print(mylist)
