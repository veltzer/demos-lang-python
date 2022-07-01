"""
Example of an enum in python3
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3


y = SampleEnum.one
print(y)
print("==============")
for x in SampleEnum:
    print(x)
print("==============")
for t in type(y):
    print(t)
