"""
An example exploring the many ways,right and wrong,to iterate
a dictionary in python.

Misconceptions:
- there were 'viewitems' and 'iteritems' members of dictionaries
in python2.7 but they are now gone in python3.
- python3's .items() is efficient (does not generated an explicit
list of key, value pairs).
- you are not allowed to change the dictionary while you are
iterating it without expecting weird results.
"""

h = {
    'keyone': 'valone',
    'keytwo': 'valtwo',
}

# this is the most efficient method
# most common and very efficient way (does not guarantee order)...
for k, v in h.items():
    print(f"key is {k}")
    print(f"val is {v}")
# each time you get BOTH a key AND value as a tuple so you can use it as a
# tuple...
for x in h.items():
    print(x)
    print(f"key is {x[0]}")
    print(f"val is {x[1]}")
# this is the same but you only get a key each time
# pylint: disable=consider-using-dict-items
for x in h:
    print(x)
    print(f"key is {x}")
    print(f"val is {h[x]}")
# this is less efficient (at least in some versions of python)
# pylint: disable=consider-iterating-dictionary
for x in h.keys():
    print(x)
    print(f"key is {x}")
    print(f"val is {h[x]}")
# this is TERRIBLE performance wise although to a novice it looks
# almost the same... Some versions of python may be smart enough to optimize
# this away but you really shouldn't count on it.
key_list = h.keys()
for x in key_list:
    print(x)
    print(f"key is {x}")
    print(f"val is {h[x]}")
