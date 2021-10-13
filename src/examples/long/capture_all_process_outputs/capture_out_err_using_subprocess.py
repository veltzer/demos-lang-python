"""
This is a program showing how to redirect both stdout and stderr for a subprocess
Notice that we get both stdout and stderr data through the same pipe.

References:
http://stackoverflow.com/questions/11495783/redirect-subprocess-stderr-to-stdout
"""

import subprocess
import sys

if len(sys.argv) < 2:
    print('must supply process to run and arguments for it', file=sys.stderr)
    sys.exit(1)

with subprocess.Popen(
    sys.argv[1:],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    shell=False
) as pr:
    for line in pr.stdout:
        line = line.decode()
        print(f"got line [{line.rstrip()}]")
