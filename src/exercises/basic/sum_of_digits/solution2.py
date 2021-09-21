#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Please specify a number", file=sys.stderr)
    sys.exit(1)


def sum_digits(n):
    sum = 0;
    while n != 0:
        sum += n % 10
        n = n // 10
    return sum


n = int(sys.argv[1])
print(sum_digits(n))
