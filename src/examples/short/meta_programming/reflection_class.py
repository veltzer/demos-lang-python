#!/usr/bin/env python

"""
This shows how to know the class that you are in...
"""

def func(A):
    print(A)


class A(object):
    a = func(A.__class__)
