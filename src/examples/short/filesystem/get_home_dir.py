"""
This is an example of how to get the home directory in python
"""

import os
from os.path import expanduser
from pathlib import Path

print(os.getenv('HOME'))
print(expanduser("~"))
print(Path.home())
