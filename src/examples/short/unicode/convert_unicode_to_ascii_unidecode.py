"""
This example shows how to convert unicode to ascii in python.

The solution here is based on the "unidecode" module.

This works for both python2 and python3.

References:
- https://pypi.python.org/pypi/Unidecode
"""

import unidecode

s = "ko\u017eu\u0161\u010dek"
print(type(s))
print(s)
t = unidecode.unidecode(s)
print(type(t))
print(t)
