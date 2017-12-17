#!/usr/bin/env python

"""
This is an example of how to do a weighted choice/sample using the
    numpy.random.choice API.

NOTES:
- the weights must sum up to 1.0 otherwise you will get the error:
    ValueError: probabilities do not sum to 1

References:
- https://stackoverflow.com/questions/10803135/weighted-choice-short-and-simple
"""

from numpy.random import choice

elements = ['one', 'two', 'three'] 
weights = [0.2, 0.3, 0.5]

print(choice(elements, p=weights, size=20))
