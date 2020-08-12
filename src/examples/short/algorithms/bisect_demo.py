"""
This example shows how to use the python bisect module
This is basically a binary search algorithm.

The problem with bisect is that it does not allow you to supply a function
to apply. This means that to use it you must maintain your own array which
contains only the values by which to look.
"""

import bisect

l = [1, 3, 4, 5, 71, 82]

print(bisect.bisect_left(l, 60))

l = [ "a", "aa", "ab", "ba", "bb" ]

print(bisect.bisect_left(l, "b"))
