#!/usr/bin/env python

"""
This is how to create temporary file names in python.
This is not a secure method and subject to race conditions, but hell,
sometimes, you don't care about security...

References:
- https://docs.python.org/3/library/tempfile.html
"""

import tempfile

for i in range(10):
    print(tempfile.mktemp())
