"""
This example deals with removing a set of characters from a string.

To sum up the results:
'translate' seems to be faster than regexp for this simple task.

References:
- https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
"""

import re
import timeit

# remove_re = re.compile("[0-9]")
# translate_map = {ord(x): None for x in "0123456789"}
remove_re = re.compile("[a-z]")
translate_map = {x: None for x in range(ord('a'), ord('z') + 1)}

line = "this 2342 is56 is the 2line"


def using_re():
    return remove_re.sub('', line)


using_re.name = 'using_re'


def using_translate():
    return line.translate(None, "abcdefghijklmnopqrstuvwzyz")


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

# print(remove_re.sub('', line))
# print(line.translate(translate_map))
