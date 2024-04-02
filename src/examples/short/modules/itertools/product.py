"""
This example shows how to use the itertools.product function
to iterate the cartesian product of two iterables.

Notes:
"""

import itertools

ll1 = [1, 2, 3]
ll2 = ["a", "b", "c", "d"]
ll3 = [True, False]

for l1, l2, l3 in itertools.product(ll1, ll2, ll3):
    print(l1, l2, l3)

for t in itertools.product(ll2, repeat=3):
    print(t)
