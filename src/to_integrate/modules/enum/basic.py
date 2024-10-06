"""
Example of an enum in python2
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


print(type(SampleEnum.one))
print(SampleEnum.one.name)
print(str(SampleEnum.one))
# convert an int to a name
print(SampleEnum(2).name)
print(SampleEnum.one.value)
# print all strings of the enum
print(SampleEnum.__members__.keys())
# prnit all enum values
print(SampleEnum.__members__.values())
# print all values as ints
print([x.value for x in SampleEnum.__members__.values()])
# find the max value
print(max(x.value for x in SampleEnum))
