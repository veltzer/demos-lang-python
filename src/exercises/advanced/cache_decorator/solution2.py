"""
solution2.py
"""

import math
from typing import Dict

# primes holds integers as keys and booleans as values
primes: Dict[int, bool] = {}


def cache(func):
    def new_is_prime(n):
        if n in primes:
            return primes[n]
        b = func(n)
        primes[n] = b
        return b
    return new_is_prime


@cache
def is_prime(n):
    print("in called")
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    while True:
        n = int(input("give me a number, -1 to end: "))
        if n == -1:
            break
        print(is_prime(n))


if __name__ == "__main__":
    main()

# test "is_prime"
# for i in range(100):
#     if is_prime(i):
#         print(i)
