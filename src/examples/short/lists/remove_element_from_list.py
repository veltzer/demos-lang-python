"""
This example shows how to remove certain elements from a list.

References:
- http://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value
"""

my_list = [1, 2, 3, 4, 2, 6, 7, 2]
# This just removes the first occurence
my_list.remove(2)
print(my_list)
# This removes all occurences
my_list = [x for x in my_list if x != 2]
print(my_list)
