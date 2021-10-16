"""
A basic example of how to use the 'attrs' framework.

Notes:
- you can construct an 'attrs' based instance with no data at all.
At runtime you can add the missing data.
- you can construct an 'attrs' based instance with partial data.
"""

from attr import attrs, attrib


@attrs
class MyObject:
    a = attrib(default=None)  # type: int
    b = attrib(default=None)  # type: int


m1 = MyObject()
m1.a = 6
m1.b = 7
print(m1)

m2 = MyObject(1, 2)
print(m2)

m3 = MyObject(b=1, a=2)
print(m3)

m4 = MyObject(b=7)
print(m4)
