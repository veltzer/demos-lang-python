"""
This example shows how to compare two lists in terms of content but not order.

References:
- https://stackoverflow.com/questions/8866652/determine-if-2-lists-have-the-same-elements-regardless-of-order
"""

list1 = ["paris", "rome", "london"]
list2 = ["rome", "london", "paris"]

assert set(list1) == set(list2)
