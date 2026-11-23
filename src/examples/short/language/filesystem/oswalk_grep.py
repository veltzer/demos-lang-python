"""
This is an example of the "os.walk" API that allows one to traverse
a directory of files recursively.
This is used to implement find(1)+grep(1) in just a few lines of python.
"""

import os.path
import re
import sys

if len(sys.argv) < 2:
    raise ValueError("please pass regexp")
c = re.compile(sys.argv[1])

for root, _dirs, files in os.walk("."):
    for file in files:
        full = os.path.join(root, file)
        with open(full) as f:
            for num, raw_line in enumerate(f):
                # remove the new line
                line = raw_line[:-1]
                for _x in c.finditer(line):
                    print(f"{full},{num}: {line}")
