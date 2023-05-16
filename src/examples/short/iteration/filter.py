"""
An example of how to use the "filter" built-in python function.

Notes:
- filter is builtin. No need to import anything.
"""

for x in filter(lambda word: len(word) == 3, {"the", "book", "import", "sup"}):
    print(x)
