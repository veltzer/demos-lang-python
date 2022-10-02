#!/usr/bin/python3

"""
This example shows how to buffer stdout
"""

import sys
import time


i = 0
print(sys.stdout.line_buffering)
while True:
    if i == 5:
        sys.stdout.reconfigure(line_buffering=False)  # type: ignore
    print(f"i is {i}...")
    time.sleep(1)
    i += 1
