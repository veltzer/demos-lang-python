"""
This example explores how to create a file with very specific mode bits.

References:
- https://stackoverflow.com/questions/5624359/write-file-with-specific-permissions-in-python/15015748
"""

import os

prev_mask = os.umask(0o000)
with os.fdopen(os.open("/tmp/test", os.O_WRONLY | os.O_CREAT, 0o644), "wt") as f:
    f.write("Hello, World!")
os.umask(prev_mask)
