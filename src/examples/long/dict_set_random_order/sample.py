"""
This is an example which shows a standard dictionary vs an ordered dict.
"""

import collections
import os

d1 = {letter: i for i, letter in enumerate("word")}
print(d1)
d2: dict[str,None] = {}
for x in dir(os):
    d2[x] = None
print(d2)
d3 = {x:None for x in dir(os)}
print(d3)
ud = {}
od = collections.OrderedDict()
s = set()
for i in range(100):
    ud[str(i)] = i
    od[str(i)] = i
    s.add(str(i))
print("unordered dict")
print(" ".join([f"{k},{v}" for k, v in ud.items()]))
print("ordered dict")
print(" ".join([f"{k},{v}" for k, v in od.items()]))
print("set")
print(" ".join(x for x in s))
