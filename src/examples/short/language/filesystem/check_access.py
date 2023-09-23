"""
This is an example of how to check access for different files.

NOTES:
- if a file does not exists os.access will return "False"
on all types of access to it and not throw an exception.
- this means that if os.access returns True it means that
    1. the file exists.
    2. the file is readable.

References:
- https://www.novixys.com/blog/python-check-file-can-read-write/
"""

import os

assert os.access("/etc/passwd", os.W_OK) is False
assert os.access("/etc/passwd", os.R_OK) is True
assert os.access("/etc/passwd", os.X_OK) is False
assert os.access("/tmp/doesnt_exist", os.R_OK) is False
assert os.access("/tmp/doesnt_exist", os.W_OK) is False
assert os.access("/tmp/doesnt_exist", os.X_OK) is False
