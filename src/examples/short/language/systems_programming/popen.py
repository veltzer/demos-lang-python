"""
This example shows how to call popen and get the return text.
"""

import os

pout = os.popen("ls -l")  # pyrefly: ignore[deprecated]  teaching: this example demonstrates os.popen itself
for number, line in enumerate(pout):
    print(number, line, end="")
