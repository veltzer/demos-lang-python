"""
This is an example of how to list all keys/values in an mdb file.

References:
- https://stackoverflow.com/questions/32489778/how-do-i-count-and-enumerate-the-keys-in-an-lmdb-with-python
"""

import lmdb
import os

# first lets create the mdb file
encoding = 'utf-8'
filename = "/tmp/sample.mdb"
if os.path.isfile(filename):
    os.unlink(filename)
env = lmdb.open(filename, subdir=False, map_size=1000000000000)
with env.begin(write=True) as txn:
    k = 'key1'.encode(encoding)
    v = 'value1'.encode(encoding)
    txn.put(k, v)
    k = 'key2'.encode(encoding)
    v = 'value2'.encode(encoding)
    txn.put(k, v)
env.close()

env = lmdb.open(filename, subdir=False, map_size=1000000000000)
with env.begin() as txn:
    with txn.cursor() as curs:
        for key, value in curs:
            print('key is: {}'.format(key.decode(encoding)))
            print('value is: {}'.format(value.decode(encoding)))

# finally lets remove the file
os.unlink(filename)
