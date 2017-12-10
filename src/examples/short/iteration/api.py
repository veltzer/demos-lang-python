#!/usr/bin/env python

"""
This example shows how to use the iterator API.
"""

r = range(10)
i = iter(r)

while True:
    try:
        print(next(i))
    except StopIteration:
        break
