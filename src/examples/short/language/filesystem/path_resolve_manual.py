"""
This is an example of how to resolve a path in python
"""

import os
import re
import sys

if len(sys.argv) < 2:
    raise ValueError("plase pass regexp")
c = re.compile(sys.argv[1])

for root, _dirs, files in os.walk("."):
    for file in files:
        full = os.path.join(root, file)
        with open(full) as f:
            for num, raw_line in enumerate(f):
                line = raw_line[:-1]
                for _x in c.finditer(line):
                    print(f"{full},{num}: {line}")
