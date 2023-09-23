"""
This example shows that if you run twice with the same seed
you get the same random numbers
"""

import random

random.seed(0)
for i in range(10):
    print(random.randrange(10))
