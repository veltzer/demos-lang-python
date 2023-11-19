"""
This example shows how stdout is configured at the beginning of your program.

Note that if you run this program on the terminal you will see that stdout is
line buffered.
If you run this program's output through a pipe you will see that it is not line
bufferd.
This is for efficiency reasons.
"""

import sys


print(sys.stdout.line_buffering)
print("Hello, World!")
