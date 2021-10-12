"""
This example shows how to shuffle a list in python

References:
http://stackoverflow.com/questions/2124347/how-to-generate-permutations-of-array-in-python
"""

import random

# to get deterministic behaviour
# random.seed(7)
my_list = list(range(1, 10))
random.shuffle(my_list)
print(my_list)
