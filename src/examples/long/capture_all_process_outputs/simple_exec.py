"""
This example only does an os.execv
"""

import os
import sys

if len(sys.argv) < 2:
    print(f"{sys.argv[0]}: must supply process to run and arguments for it", file=sys.stderr)
    print(f"{sys.argv[0]}: use it like this:", file=sys.stderr)
    print(f"{sys.argv[0]}: {sys.argv[0]} ./write_to_any.py stdout stderr tty", file=sys.stderr)
    sys.exit(1)

os.execv(sys.argv[1], sys.argv[1:])
