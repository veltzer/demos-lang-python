"""
Solution
"""

import sys

if len(sys.argv) != 2:
    print("Please specify a number", file=sys.stderr)
    sys.exit(1)


def sum_digits(n):
    n = str(n)
    my_sum = 0
    for c in n:
        my_sum += ord(c) - ord("0")
    return my_sum


def main():
    n = int(sys.argv[1])
    print(sum_digits(n))


main()
