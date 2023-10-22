"""
This is an example of how to print the name of the enum
Once it was EnumType._name_ now it's __name__.
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


print(SampleEnum.__name__)
