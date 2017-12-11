#!/usr/bin/env python

"""
This example deals with translating a set of characters from a string.

We explore two approaches:
- using re.compile and then re.sub
- using string.maketrans and then s.translate

The results:
the translation method is much faster than the regexp way. About 15 times faster!
"""

import re
import timeit
import string

remove_re = re.compile("[a-z]")
translate_map = string.maketrans(
     "".join([chr(x) for x in range(ord('a'), ord('z')+1)]),
     "".join(["-" for x in range(ord('a'), ord('z')+1)]),
)

line = "this 2342 is56 is the 2line"


def using_re():
    return remove_re.sub('-', line)


using_re.name = 'using_re'


def using_translate():
    return line.translate(translate_map)


assert using_re() == using_translate()

using_translate.name = 'using_translate'

functions = [
    using_re,
    using_translate,
]

number = 2000000

results = [(timeit.timeit(f, number=number), f.name) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print('{0:.4f}: {1}'.format(r[0], r[1]))

