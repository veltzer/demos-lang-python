"""
This shows how to run two processes in parallel
"""

import subprocess

with subprocess.Popen(["sleep", "60"]) as p1, subprocess.Popen(["sleep", "60"]) as p2:
    pass
print("I am done")
