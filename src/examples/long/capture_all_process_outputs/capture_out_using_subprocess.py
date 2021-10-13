"""
This example only captures stdout

References:
http://stackoverflow.com/questions/11495783/redirect-subprocess-stderr-to-stdout
"""

import subprocess
import sys

if len(sys.argv) < 2:
    print("must supply process to run and arguments for it", file=sys.stderr)
    sys.exit(1)

with subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE, shell=False) as pr:
    for line in pr.stdout:
        line = line.decode()
        print(f"got line [{line.rstrip()}]")
