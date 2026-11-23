"""
This example shows how to buffer stdout
"""

import io
import sys
import time

i = 0
print(sys.stdout.line_buffering)
while True:
    if i == 5:
        assert isinstance(sys.stdout, io.TextIOWrapper)
        sys.stdout.reconfigure(line_buffering=False)
    print(f"i is {i}...")
    time.sleep(1)
    i += 1
