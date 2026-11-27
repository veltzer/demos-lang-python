"""
Solution
"""


import sys
from typing import Any


class Queue:
    """
    Simple queue FIFO implementation using a python list
    """

    def __init__(self) -> None:
        self.data = []

    def push(self, item: Any) -> None:
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def len(self) -> int:
        return len(self.data)


def evaluate(exp: str):
    q = Queue()
    for c in exp.split(" "):
        if c == "*":
            q.pop()
            continue
        if c.isalpha():
            q.push(c)
            continue
        raise ValueError(f"value {c} is not supported")
    return "".join(q.data)


print(evaluate(sys.argv[1]))
