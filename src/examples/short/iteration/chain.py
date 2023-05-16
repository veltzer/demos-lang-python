"""
This example shows how to iterate two containers in sequence.

Notes:
- "chain" is supposed to be efficient in python3 but I have not
verified that.
"""

import itertools

l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]

for x in itertools.chain(l1, l2):
    print(x)
