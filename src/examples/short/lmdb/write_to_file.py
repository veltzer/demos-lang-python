"""
This is how to work with an lmdb file.
"""

import lmdb

env = lmdb.open('/tmp/file.mdb', subdir=False, map_size=1000000000000)
with env.begin(write=True) as txn:
    k = bytes('hello', 'utf8')
    v = bytes('world', 'utf8')
    txn.put(k, v)
    v = txn.get(k, default='what??')
    v = str(v, 'utf8')
    assert v == "world"
