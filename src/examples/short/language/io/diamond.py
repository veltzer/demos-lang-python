"""
This example shows how to approximate the <> operator of perl
in python.

Reminder: the <> operator (or as its called diamond) reads
all lines either specified on the command line or from standard input.

References:
- https://mail.python.org/pipermail/tutor/2005-September/041607.html
"""

import sys


def diamond_lines():
    if len(sys.argv) == 1:
        yield from sys.stdin.readlines()
    else:
        for filename in sys.argv[1:]:
            with open(filename, "rt") as file_handle:
                yield from file_handle


def main():
    for line in diamond_lines():
        print(line, end="")


if __name__ == "__main__":
    main()
