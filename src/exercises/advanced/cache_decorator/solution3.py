"""
solution3.py
"""

import math
from typing import Dict, Tuple, Any

# in cache keys are going to be (func, n) and not just n.
the_cache: Dict[Tuple[Any, Any], int] = {}


def cache(func):
    def new_func(n):
        if (func, n) in the_cache:
            return the_cache[(func, n)]
        r = func(n)
        the_cache[(func, n)] = r
        return r
    return new_func


@cache
def is_prime(n):
    print("in called")
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


@cache
def is_even(n):
    print("in called")
    return n % 2 == 0


def main():
    while True:
        n = int(input("give me a number, -1 to end: "))
        if n == -1:
            break
        print(is_prime(n))
        print(is_even(n))


if __name__ == "__main__":
    main()
# test "is_prime"
# for i in range(100):
#     if is_prime(i):
#         print(i)
