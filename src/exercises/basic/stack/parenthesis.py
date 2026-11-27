"""
parenthesis
"""

from typing import Any


class Stack:
    """
    Simple stack implementation using a python list
    """

    def __init__(self) -> None:
        self.data = []

    def push(self, item: Any) -> None:
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def len(self) -> int:
        return len(self.data)

    def top(self):
        return self.data[len(self.data) - 1]


def is_open(c: Any) -> bool:
    return c in ["(", "[", "{"]


def is_close(c: Any) -> bool:
    return c in [")", "]", "}"]


def check_match(open_braces: str, close_braces: str, pos: int) -> None:
    if open_braces == "(" and close_braces == ")":
        return
    if open_braces == "[" and close_braces == "]":
        return
    if open_braces == "{" and close_braces == "}":
        return
    raise ValueError(f"problem with parenthesis at pos {pos}")


def check_expression(exp: str) -> None:
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

# import sys  # noqa: ERA001  teaching: kept in the comment for the reader
# check_expression(sys.argv[1])  # noqa: ERA001  teaching: kept in the comment for the reader
