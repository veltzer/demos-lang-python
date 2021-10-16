"""
An example of how to use functools.partial

This is implemented the same in python2.7 and python3.
"""

import functools


def print_it(x):
    print(x)


def print_them(x, y):
    print(x, y)


def print_times(text="hello", times=1):
    for _ in range(times):
        print(text)


partial_a = functools.partial(print_it, "hello")
partial_a()

partial_b = functools.partial(print_them, "hello")
partial_b("world")

partial_c = functools.partial(print_times, times=3)
partial_c(text="hi")

partial_d = functools.partial(print_times, text="hey")
partial_d(times=2)

partial_e = functools.partial(print_times, text="ahoy", times=3)
partial_e()

partial_f = functools.partial(print_times)
partial_f("aloha", 2)
