#!/usr/bin/env python

"""
A simple example of a generator.

NOTES:
- note that the generator function can be infinite.
"""


def generate_items():
    for i in range(10):
        yield i


for x in generate_items():
    print(x)
