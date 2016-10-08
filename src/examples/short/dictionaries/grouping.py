#!/usr/bin/python3

'''
This example shows how to group data with dictionaries
'''

import collections # for defaultdict

colors = [
    'red',
    'green',
    'yellow',
    'orange',
    'blue',
    'white',
    'black',
    'purple',
    'cyan',
]

# the simple way
d={}
for color in colors:
    key=len(color)
    if key not in d:
        d[key]=[]
    d[key].append(color)
print(d)

# using 'setdefault'
d={}
for color in colors:
    key=len(color)
    d.setdefault(key, []).append(color)
print(d)

# using 'collections.defaultdict'
d=collections.defaultdict(list)
for color in colors:
    key=len(color)
    d[key].append(color)
print(d)
