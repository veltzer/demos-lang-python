"""
This example shows that iterating a hash produces random order

NOTES:
- with 'PYTHONHASHSEED' environment variable we can control the behavior
of the hash.
- 'PYTHONHASHSEED' does not guarantee traversal of elements in the
dict will be in order of insertion. It does guarantee that the order will be
the same in every run. So it guarantees determinism, not order which is
sometimes good enough.
"""


import os

print("No PYTHONHASHSEED")
os.system('./sample.py')
os.system('./sample.py')
os.environ['PYTHONHASHSEED'] = "1"
print("PYTHONHASHSEED=1")
os.system('./sample.py')
os.system('./sample.py')
