#!/usr/bin/env python

"""
This example shows that you can pass parameters to the generator
function...
"""


def generate_items(start, stop):
    for i in range(start, stop):
        yield i


for x in generate_items(2, 6):
    print(x)
