"""
This is a demo of the random.sample function
Sample draws every element at most once

References:
- https://docs.python.org/3/library/random.html
"""

from random import sample

selection = sample(range(100),k=10)
print(selection)
my_set = set(selection)
assert len(my_set) == 10
