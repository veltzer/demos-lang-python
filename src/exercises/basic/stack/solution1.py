"""
Solution1
"""


import collections
from time import thread_time


class Stack1:
    """
    First implementation. Naive using the built in python "list" data structure which offers
    everything out of the box
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


class Stack2:
    """
    Second implementation. Stack with limit on number of elements in it. The advantage of
    this is that this implementation should be more efficient than the above implementation
    """

    def __init__(self):
        self.limit = 1000
        self.data = [None] * self.limit
        self.max = 0

    def push(self, item):
        if self.max < self.limit:
            self.data[self.max] = item
            self.max += 1
        else:
            raise ValueError("stack is full")

    def pop(self):
        if self.max > 0:
            self.max -= 1
            return self.data[self.max]
        raise ValueError("stack is empty")

    def len(self):
        return self.max

    def top(self):
        return self.data[self.max - 1]


class Stack3:
    """
    Third implementation. Like second but with no checks.
    """

    def __init__(self):
        self.limit = 1000
        self.data = [None] * self.limit
        self.max = 0

    def push(self, item):
        self.data[self.max] = item
        self.max += 1

    def pop(self):
        self.max -= 1
        return self.data[self.max]

    def len(self):
        return self.max

    def top(self):
        return self.data[self.max - 1]


class Stack4:
    """
    Wrap deque to compare it to all the others
    """

    def __init__(self):
        self.deque = collections.deque()

    def push(self, item):
        self.deque.append(item)

    def pop(self):
        return self.deque.pop()

    def len(self):
        return len(self.deque)

    def top(self):
        raise ValueError("no such method")


def simple_test(s):
    s.push("Socrates")
    s.push("Plato")
    s.push("Aristotle")

    assert s.top() == "Aristotle"
    assert s.len() == 3
    assert s.pop() == "Aristotle"
    assert s.pop() == "Plato"
    assert s.pop() == "Socrates"


s1 = Stack1()
simple_test(s1)
s2 = Stack2()
simple_test(s2)
s3 = Stack3()
simple_test(s3)


# s4=Stack4()
# simple_test(s4)

def stress_test(s):
    num_of_runs = 10000
    for i in range(num_of_runs):
        num_elems = i % 900
        for j in range(num_elems):
            s.push(j)
        for j in range(num_elems):
            s.pop()


class Timer:
    def __init__(self, description: str):
        self.description: str = description
        self.start: float
        self.end: float

    def __enter__(self):
        self.start: float = thread_time()

    def __exit__(self, _type, value, traceback):
        self.end: float = thread_time()
        print(f"{self.description}: {self.end - self.start}")


do_time = True
if do_time:
    s1 = Stack1()
    s2 = Stack2()
    s3 = Stack3()
    s4 = Stack4()
    with Timer("Stack1 implementation"):
        stress_test(s1)
    with Timer("Stack2 implementation"):
        stress_test(s2)
    with Timer("Stack3 implementation"):
        stress_test(s3)
    with Timer("Stack4 implementation"):
        stress_test(s4)


def reverse_string(s):
    stack = Stack1()
    for c in s:
        stack.push(c)
    result = ""
    while stack.len():
        result += stack.pop()
    return result


def main():
    do_reverse = True
    if do_reverse:
        s = input("give me a string: ")
        print(reverse_string(s))


main()
