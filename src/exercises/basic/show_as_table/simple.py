""" simple """

import sys

for raw_line in sys.stdin:
    line = raw_line.rstrip()
    print(f"got line {line}")
