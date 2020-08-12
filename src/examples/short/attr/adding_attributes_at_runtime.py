"""
This example shows that you can add attributes at run
time to an object which is created using the 'attrs'
framework. The attribute will not be printed when printing
the instances. The attribute is accessible from outside
and from within the object and is seen in dir(object).
"""

from attr import attrs, attrib


@attrs
class MyObject(object):
    a = attrib(default=None)  # type: int
    b = attrib(default=None)  # type: int

    def add_attribute(self, val):
        # noinspection PyAttributeOutsideInit
        self.another = val

    def print(self):
        print(self.another)


m = MyObject()
m.a = 6
m.b = 7
m.add_attribute(11)

m.print()
print(m.another)
print(m)
print(dir(m))
