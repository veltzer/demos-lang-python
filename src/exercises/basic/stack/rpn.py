"""
RPN
"""


import sys


class Stack:
    """
    Simple stack implementation using a python list
    """

    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def len(self):
        return len(self.data)

    def top(self):
        return self.data[len(self.data) - 1]


def is_operator(c):
    return c in "+-*/"


def apply_operator(c, a, b):
    if c == "+":
        return a + b
    if c == "-":
        return a - b
    if c == "*":
        return a * b
    if c == "/":
        return a / b
    raise ValueError(f"strange operator {c} you have")


def evaluate(exp):
    s = Stack()
    for c in exp.split(" "):
        if is_operator(c):
            b = s.pop()
            a = s.pop()
            s.push(apply_operator(c, a, b))
            continue
        if c.isdigit():
            s.push(int(c))
            continue
    assert s.len() == 1, "Too many things on the stack"
    return s.pop()


print(evaluate(sys.argv[1]))
