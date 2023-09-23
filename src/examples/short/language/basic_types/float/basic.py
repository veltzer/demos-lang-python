"""
A basic demo of the python 'float' type

It demonstrates the arbitrary precision of floats
"""

f = 3.14
# pylint: disable=unidiomatic-typecheck
assert type(f) is float
f = 0.1**100
print(f)
