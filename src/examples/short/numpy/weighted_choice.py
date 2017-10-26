#!/usr/bin/env python

"""
This is an example of how to do a weighted choice using the
    numpy.random.choise API.

References:
- https://stackoverflow.com/questions/10803135/weighted-choice-short-and-simple
"""

from numpy.random import choice

elements = ['one', 'two', 'three'] 
weights = [0.2, 0.3, 0.5]

print(choice(elements, p=weights, size=20))
