"""
A basic example for the python built-in "filter" function

Notes:
- the function "filter" is built-in. No need to import anything.
- filter is an iterator.
"""

# make an explicit list
# pylint: disable=unnecessary-comprehension
filtered_list = [x for x in filter(lambda x: x % 2 == 1, range(10))]
print(filtered_list)

for x in filter(lambda x: x % 2 == 1, range(10)):
    print(x)
