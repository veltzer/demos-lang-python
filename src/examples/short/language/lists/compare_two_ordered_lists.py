"""
This example shows how to compare two ordered lists in python.
The full description is that we want the lists to be of the same length
and that every element in position x in the first list should be equal
to element in position x in the second list.

The short answer is to use the "==" operator for list.

References:
- https://stackoverflow.com/questions/36420022/how-can-i-compare-two-ordered-lists-in-python
"""

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2]

assert list1 == list2, "the lists are not the same"
assert list2 != list3, "the lists are the same"
