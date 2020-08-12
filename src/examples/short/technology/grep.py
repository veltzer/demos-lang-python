"""
Implementing grep in python in less than 10 lines of code...
"""

import re
import sys

# command line usage...
if len(sys.argv) < 3:
    print('usage: grep.py [expr] [files...]')
    sys.exit(1)
# first compile the regular expression...
c = re.compile(sys.argv[1])
for filename in sys.argv[2:]:
    for num, l in enumerate(open(filename)):
        if c.match(l):
            print(filename, num, l)
