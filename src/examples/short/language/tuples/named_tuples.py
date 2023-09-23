"""
Here is how to create and use named tuples in python.

References:
- https://docs.python.org/3/library/collections.html#collections.namedtuple
"""

import collections

Point = collections.namedtuple("Point", ["x", "y"])
print(type(Point))
print(dir(Point))
print(Point._fields)
p1 = Point(x=5, y=6)
print(p1)
print(type(p1))
p2 = Point(5, 6)
print(p2)
print(type(p2))
p3 = Point(5, y=6)
print(p3)
print(type(p3))
(x, y) = p3
print(x, y)
print(p3.x, p3.y)
print(Point._make([5, 6]))
# print(Point._source)
