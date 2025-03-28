""" prime_imperative_vs_functional.py """

import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def is_prime_functional(n):
    return not any(n % i == 0 for i in range(2, int(math.sqrt(n))))


print(is_prime(17))
print(is_prime(12))
print(is_prime_functional(17))
print(is_prime_functional(12))
