"""
Example of how to iterate all the values of an Enum type

If you just want the basename of the enum use .name.
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


for x in SampleEnum:
    print(type(x))
    print(x.name)
    print(x)
