"""
This example shows how to read the full content of a file in python

In order to read the entire file you must open it in binary mode.

References:
- http://stackoverflow.com/questions/7409780/reading-entire-file-in-python
"""

# Create file of 256 bytes
with open('/tmp/testfile', 'wb') as fout:
    fout.write(''.join(map(chr, range(256))).encode())

# Text mode
with open('/tmp/testfile') as fin:
    print('Opened in text mode is:', len(fin.read()))
    # Opened in text mode is: 26

# Binary mode - note 'rb'
with open('/tmp/testfile', 'rb') as fin:
    print('Opened in binary mode is:', len(fin.read()))
    # Opened in binary mode is: 256
