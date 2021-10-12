"""
This is an example which shows a standard dictionary vs an ordered dict.
"""

import collections
import os

d = dict((letter, i) for i, letter in enumerate('word'))
print(d)
d = {}
for x in dir(os):
    d[x] = None
# d = {x:None for x in dir(os)}
print(d)
ud = {}
od = collections.OrderedDict()
s = set()
for i in range(100):
    ud[str(i)] = i
    od[str(i)] = i
    s.add(str(i))
print('unordered dict')
print(' '.join(['{k},{v}'.format(k=k, v=v) for k, v in ud.items()]))
print('ordered dict')
print(' '.join(['{k},{v}'.format(k=k, v=v) for k, v in od.items()]))
print('set')
print(' '.join([x for x in s]))
