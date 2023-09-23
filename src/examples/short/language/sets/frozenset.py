"""
This example shows the difference between set and frozenset.

Notes:
- you cannot modify a frozen set. It does not support the "add" and "remove" methods.
- if you try to put a set into a set then you get an error since set is non hashable.
- the hash code of frozenset(a,b) is the same as the hash code for frozenset(b,a)
the result of which is that if you put frozenset(b,a) into a set which already contains
frozenset(a,b) then you dont actually change the set.
"""

# frozenset does not support "add"
try:
    set_a: frozenset = frozenset()
    set_a.add("a")  # type: ignore
except AttributeError:
    print("yes, got AttributeError")

# frozenset does not support "remove"
try:
    set_b: frozenset = frozenset()
    set_b.remove("a")  # type: ignore
except AttributeError:
    print("yes, got AttributeError")

try:
    set_c = set()
    set_c.add({"a", "b"})
    set_c.add({"b", "a"})
except TypeError:
    print("yes, got TypeError")

# same thing with frozenset
set_d = set()
set_d.add(frozenset(["a", "b"]))
set_d.add(frozenset(["b", "a"]))
set_d.add(frozenset(["a", "b"]))
set_d.add(frozenset(["b", "a"]))
print(set_d)
