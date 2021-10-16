"""
This is an example of how to resolve a path in python
"""

import os
import re
import sys

if len(sys.argv) < 2:
    raise ValueError('plase pass regexp')
c = re.compile(sys.argv[1])

for root, dirs, files in os.walk('.'):
    for file in files:
        full = os.path.join(root, file)
        with open(full) as f:
            for num, line in enumerate(f):
                line = line[:-1]
                for x in c.finditer(line):
                    print(f"{full},{num}: {line}")
