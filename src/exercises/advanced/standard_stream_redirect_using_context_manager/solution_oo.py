"""
solution_oo
"""

import sys


class RedirectManager:

    def __init__(self, filename):
        print("in __init__", file=sys.stderr)
        self.filename = filename
        self.old_output = None

    def __enter__(self):
        print("in __enter__", file=sys.stderr)
        self.old_output = sys.stdout
        sys.stdout = open(self.filename, "wt")

    def __exit__(self, exception_type, value, traceback):
        print("in __exit__", file=sys.stderr)
        sys.stdout.close()
        sys.stdout = self.old_output


print("You should see this on your screen")
with RedirectManager("/tmp/log.txt"):
    print("You really shouldnt see this on your screen")
    raise ValueError("dummy value")
print("You should see this on your screen")
