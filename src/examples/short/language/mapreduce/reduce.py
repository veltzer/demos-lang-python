""" reduce.py """

import sys

last = None
count = 0
for raw_line in sys.stdin:
    line = raw_line.rstrip()
    if line == last:
        count += 1
    else:
        if last is not None:
            print(last, count)
        last = line
        count = 1
