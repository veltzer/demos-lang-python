"""
This is an improvement on the previous singleton example.
This time we protect against concurrent access.
"""

from __future__ import annotations

import threading
from typing import ClassVar


class A:
    instance: ClassVar[A | None] = None

    def __init__(self):
        if A.instance is not None:
            raise ValueError("you called the constructor twice!!")
        # constructor code goes here
        print("in A constructor")
        self.my_attribute = "value"

    lock = threading.Lock()

    @staticmethod
    def get_instance() -> A | None:
        with A.lock:
            if A.instance is None:
                A.instance = A()
            return A.instance


a1 = A.get_instance()
a2 = A.get_instance()
if a1 is a2:
    print("yes,they are the same instance")
print(a1)
print(a2)
print(dir(a1))
print(dir(a2))
