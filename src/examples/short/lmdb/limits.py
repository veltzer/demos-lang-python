"""
Testing the limits of lmdb

results:
- keys must be <= 512
- values do not have a limit on them.
"""

import lmdb

env = lmdb.open('/tmp', map_size=1000000000000)
with env.begin(write=True) as txn:
    try:
        k = bytes('a' * 700, 'utf8')
        v = bytes('world', 'utf8')
        txn.put(k, v)
    except lmdb.BadValsizeError:
        print("yes, got an exception, keys must be less than 512")
    # this will work, values do not have limitations
    k = bytes('world', 'utf8')
    v = bytes('a' * 7000000, 'utf8')
    txn.put(k, v)
