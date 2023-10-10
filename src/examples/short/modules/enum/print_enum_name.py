"""
This is an example of how to print the name of the enum
Once is was EnumType._name_
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


print(SampleEnum.__name__)
