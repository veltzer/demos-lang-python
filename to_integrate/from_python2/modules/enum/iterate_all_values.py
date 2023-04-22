"""
This example shows how to iterate all the values of an enum type
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

# This works but the problem is that pycharm complains about it
for x in SampleEnum:
    print('actual enum value is [{}]'.format(x))
    print('int is [{}]'.format(x.value))
    print('name is [{}]'.format(x.name))

# pycharm does not complain about this one...
for x in SampleEnum.__members__.values():
    print('actual enum value is [{}]'.format(x))
    print('int is [{}]'.format(x.value))
    print('name is [{}]'.format(x.name))
