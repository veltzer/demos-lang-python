"""
This example deals with removing a set of characters from a string.

We examine two approaches:
- s.replace
- re.compile and then re.sub

* In python2 we could have used the 'maketrans' and 'translate' approach but translate
cannot be used to remove a string in python3.

References:
- https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
"""

import re
import timeit

remove_re = re.compile("[a-z]")

line = "this 2342 is56 is the 2line"

function_names = {}


def remove_many(s, list_of_chars):
    for x in list_of_chars:
        s = s.replace(x, "")
    return s


def using_re():
    return remove_re.sub('', line)


function_names[using_re] = 'using_re'


def using_replace():
    return remove_many(line, "abcdefghijklmnopqrstuvwxyz")


function_names[using_replace] = 'using_replace'

assert using_re() == using_replace()

functions = [
    using_re,
    using_replace,
]

number = 2000000

results = [(timeit.timeit(f, number=number), function_names[f]) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print(f"{r[0]:.4f}: {r[1]}")
