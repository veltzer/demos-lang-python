#!/usr/bin/env python

"""
This is an example of how to get the home directory in python
"""

import os

print(os.getenv('HOME'))

from os.path import expanduser
print(expanduser("~"))

from pathlib import Path
print(Path.home())
