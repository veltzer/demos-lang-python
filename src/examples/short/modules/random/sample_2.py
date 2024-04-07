"""
This is a demo of the random.sample function with counts

References:
- https://docs.python.org/3/library/random.html
"""

from random import sample

colors: list[str] = ["r", "g", "b"]

# counts multiplies each element in color by the relative count
print(sample(colors, k=5, counts=(10,20,5)))
