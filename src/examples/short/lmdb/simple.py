"""
A basic demo of the lmdb module

By default the files that will be created in the folder you specify
are "data.mdb" and "lock.mdb".
"""

import lmdb

env = lmdb.open("/tmp", map_size=1000000000000)
with env.begin(write=True) as txn:
    k1_b = bytes("hello", "utf8")
    v1_b = bytes("world", "utf8")
    txn.put(k1_b, v1_b)
    v_b = txn.get(k1_b, default="what??")
    v = str(v_b, "utf8")
    assert v == "world"

# The next code does not work
# env=lmdb.open("/tmp/file.mdb", subdir=False, max_dbs=2)
# with env.begin(write=True, db="a") as txn:
#     k=bytes("a_key","utf8")
#     v=bytes("a_val","utf8")
#     txn.put(k,v)
#
# with env.begin(write=False, db="a") as txn:
#     v=txn.get("a_key")
#     v=str(v,"utf8")
#     assert v == "a_val"
