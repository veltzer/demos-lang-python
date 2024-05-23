"""
This is an example of how to use the subprocess module for streaming
"""

import subprocess

with subprocess.Popen(
    ["python", "process.py"],
    shell=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
) as p:
    # next line is to assert that p.stdout is not None for pylint to be sure that it can be iterated
    # on the next line
    assert p.stdout is not None
    password = None
    for line in p.stdout:
        if line.startswith("secret="):
            password = line[7:-1]
    p.wait()
    print(f"Whooo hooo! I got the passowrd and it is {password}")
