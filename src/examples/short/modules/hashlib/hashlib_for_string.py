"""
This is an example of how to write a simple md5 sum function in python

References:
- https://docs.python.org/3/library/hashlib.html
"""

import hashlib


def md5_string(s: str) -> str:
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()


print(md5_string("hello"))
