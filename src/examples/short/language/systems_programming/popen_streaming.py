"""
This example shows how to call popen and get the return text.
"""

import os

# mode="r" is the default
pout = os.popen("./demo_process.py")  # pyrefly: ignore[deprecated]  teaching: this example demonstrates os.popen itself
for line in pout:
    print("line is", line, end="")
