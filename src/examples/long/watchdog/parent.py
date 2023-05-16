"""
This is the parent process. It is the watchdog.
It use the "subprocess" module to run the child.
"""

import subprocess

while True:
    print("this is the parent running the child")
    code = subprocess.call(["python3", "child.py"])
    print(f"this is the parent, got code {code}")
