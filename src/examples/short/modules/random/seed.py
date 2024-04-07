"""
This demos the seed function

References:
- https://docs.python.org/3/library/random.html
"""

from random import seed, random, randint, sample

seed(1)

print(f"{random() = }")
print(f"{randint(1, 5) = }")
print(f"{sample(range(1000), k=5) = }")
