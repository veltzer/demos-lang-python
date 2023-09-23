"""
This example shows how to use flush

Notes:
- there is no way that I know of not to end a print with a newline and flush using
only the "print" function.
- this means you do need to add the "sys.stdout.flush()" to see things.
"""

import sys
import time

print("Hello", end="")
time.sleep(5)
sys.stdout.flush()
