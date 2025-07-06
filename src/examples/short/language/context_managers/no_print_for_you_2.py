import sys
import os

class SuppressPrint:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

# Usage
print("This shows")
with SuppressPrint():
    print("This is hidden")
    print("So is this")
print("This shows again")
