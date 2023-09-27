"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""

import time
from functools import cache


@cache
def calc_sum(i):
    my_sum = 0
    for j in range(i):
        time.sleep(0.5)
        my_sum += j
    return my_sum


print(calc_sum(6))
print(calc_sum(7))

print(calc_sum(6))
print(calc_sum(7))
