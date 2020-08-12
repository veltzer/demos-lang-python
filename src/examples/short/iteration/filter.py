"""
An example of how to use the 'filter' built-in python function.

Notes:
- filter is builtin. No need to import anything.
"""

for x in filter(lambda x: len(x) == 3, {"abc", "abcd", "cbcdef", "yui"}):
    print(x)
