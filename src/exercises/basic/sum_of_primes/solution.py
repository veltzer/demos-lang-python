"""
Solution
"""

import math


def is_prime(n):
    return all(n % j != 0 for j in range(2, int(math.sqrt(n)) + 1))


my_sum = 0
for i in range(2,1000000):
    if is_prime(i):
        my_sum += i
print(f"sum is {my_sum}")
