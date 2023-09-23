"""
How to use infinite in python.

Note that math.inf is intimately connected with math.nan since, for instance,
math.inf/math.inf=math.nan

References:
- https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
"""

import math

print(math.inf)
print(-math.inf)
print(-math.inf / 2)
print(math.inf * 2)
print(math.inf - math.inf)
print(math.inf / math.inf)
print(math.nan)
