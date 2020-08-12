"""
This is an example of comparing the performance of list vs tuple vs
set vs frozenset
"""

import timeit

n = 1000
repetitions = 1
l = [str(k) for k in range(n)]
s = set(l)
f = frozenset(l)
t = tuple(l)


def demo_list():
    return [value in l for value in l]


def demo_set():
    return [value in s for value in l]


def demo_frozenset():
    return [value in f for value in l]


def demo_tuple():
    return [value in t for value in l]


print("list {:.04f}".format(timeit.timeit(demo_list, number=repetitions)))
print("set {:.04f}".format(timeit.timeit(demo_set, number=repetitions)))
print("frozenset {:.04f}".format(timeit.timeit(demo_frozenset, number=repetitions)))
print("tuple {:.04f}".format(timeit.timeit(demo_tuple, number=repetitions)))
