"""
This is a simple example of how to get random numbers in python.

Randrange can be used with just stop, start/stop, or start/stop/step
parameters.

References:
- https://docs.python.org/3/library/random.html
"""

import random

for i in range(10):
    print(random.randrange(10))
print("=========")
for i in range(10):
    print(random.randrange(15, 20))
print("=========")
for i in range(10):
    print(random.randrange(-20, -10, 2))
