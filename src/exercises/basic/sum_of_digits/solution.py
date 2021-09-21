#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Please specify a number", file=sys.stderr)
    sys.exit(1)


def sum_digits(n):
    n = str(n)
    sum = 0
    for c in n:
        sum += ord(c)-ord('0')
    return sum


n = int(sys.argv[1])
print(sum_digits(n))
