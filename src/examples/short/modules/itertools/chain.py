"""
This example shows how to iterate two containers in sequence.

Notes:
- "chain" is supposed to be efficient in python3 but I have not
verified that.
"""

import itertools

l1 = range(0, 5000) 
l2 = range(6000, 90000)

for x in itertools.chain(l1, l2):
    print(x)
