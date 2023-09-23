"""
Implementing grep in python in less than 10 lines of code...

Use it this way: grep.py mark /etc/passwd
"""

import re
import sys

# command line usage...
if len(sys.argv) < 3:
    print("usage: grep.py [expr] [files...]")
    sys.exit(1)
# first compile the regular expression...
c = re.compile(sys.argv[1])
for filename in sys.argv[2:]:
    with open(filename) as f:
        for num, line in enumerate(f):
            if c.match(line):
                print(f"{filename},{num}: {line}", end="")
