#!/usr/bin/python3

"""
Demo how to create a temp file in python

References:
- https://docs.python.org/3/library/tempfile.html
"""

import tempfile  # for NamedTemporaryFile
import os.path  # for isfile

# delete=True is the default...
with tempfile.NamedTemporaryFile(mode="wt") as t:
    name = t.name
    print('name is [{0}]'.format(t.name))
    print("hello, world!", file=t)
assert not os.path.isfile(name)

with tempfile.NamedTemporaryFile(mode="wt", delete=False) as t:
    name = t.name
    print('name is [{0}]'.format(t.name))
    print("hello, world!", file=t)
assert os.path.isfile(name)
