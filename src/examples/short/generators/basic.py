#!/usr/bin/env python

"""
Another basic example of a generator
"""


def give_me_some_data():
    yield 7
    yield -14
    yield True


for x in give_me_some_data():
    print(x)
