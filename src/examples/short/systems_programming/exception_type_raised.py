"""
This example investigates which error is raised when a child fails.

The result is that the exception type is 'subprocess.CalledProcessError'.
"""

import subprocess

try:
    subprocess.check_call(['ls', 'nonexistant'], stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    print('yes, got exception')
