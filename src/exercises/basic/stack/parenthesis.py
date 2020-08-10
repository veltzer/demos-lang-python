#!/usr/bin/env python3


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
        return self.data[len(self.data)-1]


def is_open(c):
    return c=='(' or c=='[' or c=='{'

def is_close(c):
    return c==')' or c==']' or c=='}'

def check_match(open_braces, close_braces, pos):
    if open_braces=='(' and close_braces==')':
        return
    if open_braces=='[' and close_braces==']':
        return
    if open_braces=='{' and close_braces=='}':
        return
    raise ValueError("problem with parenthesis at pos {}".format(pos))
  

def check_expression(exp):
    s=Stack()
    for pos, c in enumerate(exp):
        if is_open(c):
            s.push(c)
            continue
        if is_close(c):
            last_open=s.pop()
            check_match(last_open, c, pos)

            continue
        raise ValueError("what is {} at position {}?".format(c, pos))
    assert s.len()==0, "opened parenthesis at end of expression"

check_expression("[]")
check_expression("")
check_expression("{[()]}")

# import sys
# check_expression(sys.argv[1])
