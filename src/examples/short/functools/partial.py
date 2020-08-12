"""
An example of how to use functools.partial

This is implemented the same in python2.7 and python3.
"""

import functools


def print_it(x):
    print(x)


f = functools.partial(print_it, "hello")
f()


def print_them(x, y):
    print(x, y)


g = functools.partial(print_them, "hello")
g("world")


def print_times(text="hello", times=1):
    for i in range(times):
        print(text)


h = functools.partial(print_times, times=3)
h(text="hi")

i = functools.partial(print_times, text="hey")
i(times=2)

j = functools.partial(print_times, text="ahoy", times=3)
j()

h = functools.partial(print_times)
h("aloha", 2)
