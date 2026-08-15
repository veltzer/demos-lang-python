"""
This is how to work with an lmdb file.
"""

import lmdb

env = lmdb.open("/tmp/file.mdb", subdir=False, map_size=1000000000000)
with env.begin(write=True) as txn:
    k1_b = bytes("hello", "utf8")
    v1_b = bytes("world", "utf8")
    txn.put(k1_b, v1_b)
    v_b = txn.get(k1_b, default="what??")  # pyrefly: ignore[no-matching-overload]
    v = str(v_b, "utf8")  # type: ignore[arg-type] # pyrefly: ignore[no-matching-overload]
    assert v == "world"
