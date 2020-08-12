"""
This is an example which shows a stadard dictionary vs an ordered dict.
"""

import collections
import os
import sys

d = dict((L, i) for i, L in enumerate('abcd'))
print(d)
sys.exit(0)
d = dict()
for x in dir(os):
    d[x] = None
# d = {x:None for x in dir(os)}
print(d)
sys.exit(0)
ud = dict()
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
