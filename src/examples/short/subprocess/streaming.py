"""
This is an example of how to use the subprocess module for streaming
"""

import subprocess

with subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE) as p:
    for line in p.stdout:
        print(line.decode().rstrip())
