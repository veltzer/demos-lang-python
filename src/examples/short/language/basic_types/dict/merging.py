"""
This example shows how to merge dictionaries

There are two ways:
- the d.update() method of dictionaries
- the collections.ChainMap class.
"""

import collections

d1 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}

d2 = {
    "two": -2,
    "three": -3,
    "five": 5,
}

d3 = {
    "two": -4,
    "three": -6,
    "one": -1,
}

d_1 = d1.copy()
d_1.update(d2)
d_1.update(d3)
print(d_1)

d_2 = collections.ChainMap(d3, d2, d1)
print(d_2)

print(d_1 == d_2)
