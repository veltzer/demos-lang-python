"""
This is an example of adding methods to an enum.
"""

import enum


class SampleEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

    def do_something(self):
        print(self)


SampleEnum.one.do_something()
