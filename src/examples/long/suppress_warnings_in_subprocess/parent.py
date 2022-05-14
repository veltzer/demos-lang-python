"""
An example of how a parents can suppress warnings in a child process
"""

import subprocess
import os


print("one")
subprocess.check_call(["python3", "child.py"])
os.environ["PYTHONWARNINGS"]="ignore"
print("two")
subprocess.check_call(["python3", "child.py"])
os.environ["PYTHONWARNINGS"]="default"
print("three")
subprocess.check_call(["python3", "child.py"])
