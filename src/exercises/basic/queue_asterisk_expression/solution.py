"""
Solution
"""


import sys


class Queue:
    """
    Simple queue FIFO implementation using a python list
    """

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def len(self):
        return len(self.data)


def evaluate(exp):
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
