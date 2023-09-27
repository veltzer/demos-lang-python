"""
This is an example of how to use the subprocess module for streaming
"""

import subprocess

with subprocess.Popen(
    ["python", "process.py"],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
) as p:
    assert p.stdout is not None
    for line_b in p.stdout:
        line = line_b.decode().rstrip()
        if line.startswith("secret="):
            password = line[7:]
    p.wait()
    print(f"Whooo hooo! I got the passowrd and it is {password}")
