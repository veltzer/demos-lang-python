"""
This example shows how to list all elements of a gdbm file.

Notes:
- order of traversal is not in order of insertion.
- a gdbm handle does not supply all of the standard python dict abstraction
and them 'items' iterator.
"""

import dbm.gnu

filename = "/tmp/test.gdbm"
# 'r' means open just for reading
d = dbm.gnu.open(filename, 'r')

# lets try iterating with .items()
try:
    for _k, _v in d.items():
        pass
except AttributeError as _:
    print("nope, you cannot use 'items' on a gdbm handle")

# show all key value pairs
k = d.firstkey()
while k is not None:
    print(k.decode(), d[k].decode())
    k = d.nextkey(k)

d.close()
