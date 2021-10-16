"""
This example shows how to launch a process asynchronously in python

References:
- http://stackoverflow.com/questions/636561/how-can-i-run-an-external-command-asynchronously-from-python
"""

import subprocess
import time

with subprocess.Popen(['watch', 'ls']) as p:
    time.sleep(10)
    p.terminate()
