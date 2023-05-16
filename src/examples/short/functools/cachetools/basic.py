"""
A basic example for using the "functools" module

References:
- https://docs.python.org/3/library/functools.html#functools.lru_cache
"""

import time
from functools import lru_cache


@lru_cache(maxsize=1000)
def my_function(a, b):
    time.sleep(2)
    return a + b


print(my_function(2, 3))
print(my_function(2, 3))
