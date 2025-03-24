"""
parenthesis
"""

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


def is_open(c):
    return c in ["(", "[", "{"]


def is_close(c):
    return c in [")", "]", "}"]


def check_match(open_braces, close_braces, pos):
    if open_braces == "(" and close_braces == ")":
        return
    if open_braces == "[" and close_braces == "]":
        return
    if open_braces == "{" and close_braces == "}":
        return
    raise ValueError(f"problem with parenthesis at pos {pos}")


def check_expression(exp):
    s = Stack()
    for pos, c in enumerate(exp):
        if is_open(c):
            s.push(c)
            continue
        if is_close(c):
            last_open = s.pop()
            check_match(last_open, c, pos)

            continue
        raise ValueError(f"what is {c} at position {pos}?")
    assert s.len() == 0, "opened parenthesis at end of expression"


check_expression("[]")
check_expression("")
check_expression("{[()]}")

# import sys
# check_expression(sys.argv[1])
