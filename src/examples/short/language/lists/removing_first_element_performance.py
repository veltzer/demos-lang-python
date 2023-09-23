"""
This example proves that adding to the start of a list, removing from the start of a list
are very expensive operations.

It also shows that the same operations on a "collections.deque" data structure are very
efficient.
"""

import collections
import timeit


function_names = {}


def func1():
    del my_list[0]


function_names[func1] = "del list[0]"


def func2():
    my_list.pop(0)


function_names[func2] = "list.pop(0)"


def func3():
    my_list.insert(0, "newelem")


function_names[func3] = "insert(0, newelement)"


def func4():
    del d[0]


function_names[func4] = "del deque[0]"


def func5():
    d.popleft()


function_names[func5] = "deque.popleft()"


def func6():
    d.appendleft("newelem")


function_names[func6] = "deque.appendleft(newelement)"

my_list = list(range(1000000))
d = collections.deque(range(1000000))

functions = [
    func1,
    func2,
    func3,
    func4,
    func5,
    func6,
]

number = 1000
results = [(timeit.timeit(f, number=number), function_names[f]) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print(f"{r[0]:.4f}: {r[1]}")
