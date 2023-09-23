"""
This example shows that when you run python the path to the script you are running
is added to the search path for modules (aks PYTHONPATH).
Note that it is NOT the current directory that is added, although they are sometimes
the same.
"""

import sys

print(sys.path)
