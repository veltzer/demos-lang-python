"""
solution.py
"""

import math


def is_prime(n: int) -> bool:
    return all(n % i != 0 for i in range(2, int(math.sqrt(n) + 1)))


# test is_prime
# for i in range(100):
#     if is_prime(i):
#         print(i)  # noqa: ERA001  teaching: kept in the comment for the reader
