"""
This is an improvement on the previous singleton example.
This time we make the singleton access method a static method
and not just a global function.

Notes:
- In this example we do not protect against concurrent access.
"""

import typing


class A:
    instance = None  # type: A

    def __init__(self):
        if A.instance is not None:
            raise ValueError("you called the constructor twice!!")
        # constructor code goes here
        print("in A constructor")
        self.my_attribute = "value"

    @classmethod
    def get_instance(cls) -> typing.Union["A", None]:
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance


a1 = A.get_instance()
a2 = A.get_instance()
if a1 is a2:
    print("yes,they are the same instance")
print(a1)
print(a2)
print(dir(a1))
print(dir(a2))
