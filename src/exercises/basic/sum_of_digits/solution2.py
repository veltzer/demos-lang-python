"""
Solution2
"""

import sys

if len(sys.argv) != 2:
    print("Please specify a number", file=sys.stderr)
    sys.exit(1)


def sum_digits(n):
    my_sum = 0
    while n != 0:
        my_sum += n % 10
        n = n // 10
    return my_sum


def main():
    n = int(sys.argv[1])
    print(sum_digits(n))


main()
