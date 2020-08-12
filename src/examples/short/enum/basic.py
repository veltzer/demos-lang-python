"""
Example of an enum in python3
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

# this is how to get the enum value (which is not the same as the int or the string)
print(type(SampleEnum.one))
# this is how to get the int value
print(type(SampleEnum.one.value))
# this is how to get the string name
print(type(SampleEnum.one.name))
