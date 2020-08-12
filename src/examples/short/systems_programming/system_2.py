"""
This example demonstrates how to analyze the return code of a child process.
"""

import os

ret = os.system('ls -l >/dev/null')
print(ret)
ret = os.system('ls -l sdfsdf >/dev/null')
print(ret)
