"""
This example explores what happens when you modify the dictionary while
you are iterating it.

Conclusions:
- passing over d and d.keys() is the same as far as modification during
iteration.
"""

d = {}
for i in range(10):
    d[i] = i

# if the dictionary changes size during iteration you get a RuntimeError
# you get the exception as soon as you use the iterator after modifying
# the size of the dictionary
# this means that the iterator saves the size of the dictionary and
# compares the size of the dictionary with it's own size every iteration.
visited_keys = set()
try:
    for x in d:
        if x == 3:
            del d[5]
        visited_keys.add(x)
except RuntimeError as e:
    assert str(e) == 'dictionary changed size during iteration'
    assert len(visited_keys) == 4

d = {}
for i in range(10):
    d[i] = i

# what if we removed items and added items in the same amount?
# we do not get an exception.
# the result is that we pass over the keys with the modifications.
visited_keys = set()
for x in d:
    if x == 3:
        del d[5]
        d[10] = 10
    visited_keys.add(x)
assert len(visited_keys) == 10
assert 5 not in visited_keys
assert 10 in visited_keys

d = {}
for i in range(10):
    d[i] = i

# what if we pass over d.keys() and not just d?
# we still get the exception if we change the number of elements
visited_keys = set()
try:
    # pylint: disable=consider-iterating-dictionary
    for x in d.keys():
        if x == 3:
            del d[5]
        visited_keys.add(x)
except RuntimeError as e:
    assert str(e) == 'dictionary changed size during iteration'
    assert len(visited_keys) == 4

d = {}
for i in range(10):
    d[i] = i

# what if we pass over d.keys() and make sure to keep the same amount of elements?
visited_keys = set()
# pylint: disable=consider-iterating-dictionary
for x in d.keys():
    if x == 3:
        del d[5]
        d[10] = 10
    visited_keys.add(x)
assert len(visited_keys) == 10
assert 5 not in visited_keys
assert 10 in visited_keys

d = {}
for i in range(10):
    d[i] = i

# what if we store d.keys() and pass over that?
# this does not help. when you do l=d.keys() you don't
# get a copy of all the keys but rather a special object
# which behaves likes the keys but points to the original
# dictionary...
my_list = d.keys()
assert my_list.__class__.__name__ == 'dict_keys'
visited_keys = set()
try:
    for x in my_list:
        if x == 3:
            del d[5]
        visited_keys.add(x)
except RuntimeError as e:
    assert str(e) == 'dictionary changed size during iteration'
    assert len(visited_keys) == 4

d = {}
for i in range(10):
    d[i] = i

# what if we build a list from the keys?
# in this case we actually iterate all the original keys from the original
# hash, regardless of modification
# in this case, we must be careful when accessing the dictionary...
my_list = list(d.keys())
assert isinstance(my_list, list)
visited_keys = {}
for x in my_list:
    if x == 3:
        del d[5]
    if x in d:
        visited_keys[x] = d[x]
assert len(visited_keys) == 9
assert 5 not in visited_keys
