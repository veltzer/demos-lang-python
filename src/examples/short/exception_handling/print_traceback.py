#!/usr/bin/env python

"""
This example shows how to print a traceback
"""
from traceback import print_exc

try:
    raise ValueError('hello')
except ValueError as e:
    print_exc()
