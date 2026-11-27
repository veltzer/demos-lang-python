""" prime_imperative_vs_functional.py """

import math


def is_prime(n: int) -> bool:
    return all(n % i != 0 for i in range(2, int(math.sqrt(n))))


def is_prime_functional(n: int) -> bool:
    return not any(n % i == 0 for i in range(2, int(math.sqrt(n))))


print(is_prime(17))
print(is_prime(12))
print(is_prime_functional(17))
print(is_prime_functional(12))
