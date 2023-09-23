"""
A basic demo of the python 'int' type

It demonstrates the arbitrary precision of ints
"""

i = 3
# pylint: disable=unidiomatic-typecheck
assert type(i) is int
i = 10**100
print(i)
