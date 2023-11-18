"""
This example shows the various ways to create a list in python

References:
- https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/
"""

# explicit list
list1 = [1, 2, 3, 4]
print(list1)

# empty list with constructur
# pylint: disable=use-list-literal
list2 = list()  # type: ignore
print(list2)

# empty list explicit
list3 = []  # type: ignore
print(list3)

# from another list
list4 = list([1,2,3])
print(list4)

# from a tuple
list5 = list((1,2,3))
print(list5)
