"""
This is an example that shows how to calculate the relative paths of one path to the other.
"""

import os.path

print(os.path.relpath('/etc/passwd', '/etc'))
