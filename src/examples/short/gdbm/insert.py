"""
This is a simple example of how to use the dbm.gnu module of the
standard python library

NOTES:
- the attempt to insert 'None' as value or key throws an exception.
- anything which is given to gdbm is converted to bytes, so
    if you have bytes do not convert them to strings (they will
    just be converted back again).
- empty strings or bytes are allowed as both values and keys.
"""

import dbm.gnu
import os.path

# the 'c' in the next row means open rw and create if it doesn't exist
filename = "/tmp/test.gdbm"

if os.path.isfile(filename):
    os.unlink(filename)

# n means create a new database and open for reading and writing
d = dbm.gnu.open(filename, 'n')
d['one'] = 'ehad'
d['two'] = 'shtaim'
d[b''] = b'emptybytes'
d[b'emptybytes'] = b''
d[''] = 'emptystring'
d['emptystring'] = ''
try:
    # noinspection PyTypeChecker
    d['three'] = None
except TypeError:
    print("yes, got exception when trying to put None as value")
try:
    # noinspection PyTypeChecker
    d[None] = 'four'
except TypeError:
    print("yes, got exception when trying to put string as key")
d['five'] = 'five'.encode()
d.close()
