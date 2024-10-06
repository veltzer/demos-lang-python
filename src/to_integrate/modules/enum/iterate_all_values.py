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
    print(f"actual enum value is [{x}]")
    print(f"int is [{x.value}]")
    print(f"name is [{x.name}]")


# pycharm does not complain about this one...
for x in SampleEnum.__members__.values():
    print(f"actual enum value is [{x}]")
    print(f"int is [{x.value}]")
    print(f"name is [{x.name}]")
