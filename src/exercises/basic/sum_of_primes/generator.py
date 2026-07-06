"""
Generator based solution
"""

import math
import itertools


def primes():
    yield 2
    for n in itertools.count(3, 2):
        if all(n % j for j in range(3, int(math.sqrt(n)) + 1, 2)):
            yield n


my_sum = sum(itertools.takewhile(lambda p: p < 1000000, primes()))
print(f"sum is {my_sum}")
