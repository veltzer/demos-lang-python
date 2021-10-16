"""
This example shows how to split a filename into its components.

NOTES:
- split is just like (dirname, basename)
- splitext is for extensions.
"""

import os.path
import sys

for line in sys.stdin:
    line = line.strip()
    print(f"basename is [{os.path.basename(line)}]")
    print(f"dirname is [{os.path.dirname(line)}]")
    print(f"splitext is [{os.path.splitext(line)}]")
    print(f"split is [{os.path.split(line)}]")
