import sys
from contextlib import contextmanager

@contextmanager
def suppress_print():
    with open('/dev/null', 'w') as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

# Usage
print("This will be shown")
with suppress_print():
    print("This will NOT be shown")
    print("Neither will this")
print("This will be shown again")
