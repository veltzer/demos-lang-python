"""
This example shows the difference between set and frozenset.

Notes:
- you cannot modify a frozen set. It does not support the 'add' and 'remove' methods.
- if you try to put a set into a set then you get an error since set is non hashable.
- the hash code of frozenset(a,b) is the same as the hash code for frozenset(b,a)
the result of which is that if you put frozenset(b,a) into a set which already contains
frozenset(a,b) then you don't actually change the set.
"""

# frozenset does not support 'add'
try:
    set_a = frozenset()
    set_a.add('a')
except AttributeError as e:
    print('yes, got AttributeError')

# frozenset does not support 'remove'
try:
    set_a = frozenset()
    set_a.remove('a')
except AttributeError as e:
    print('yes, got AttributeError')

try:
    set_a = set()
    set_a.add({'a', 'b'})
    set_a.add({'b', 'a'})
except TypeError as e:
    print('yes, got TypeError')

# same thing with frozenset
set_b = set()
set_b.add(frozenset(['a', 'b']))
set_b.add(frozenset(['b', 'a']))
set_b.add(frozenset(['a', 'b']))
set_b.add(frozenset(['b', 'a']))
print(set_b)
