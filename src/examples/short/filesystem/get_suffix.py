"""
This example shows how to get the suffix of a filename in python3.

References:
- https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
"""

import os.path
import sys


def get_suffix(filename:str) -> str:
    return os.path.splitext(filename)[1]

for line in sys.stdin:
    line = line.rstrip()
    print(f"suffix is [{get_suffix(line)}]")
