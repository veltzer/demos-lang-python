"""
This example shows that you cannot use the return value of the 'map' function
directly. Instead you must either use a "for" loop to extract the values or
to construct some data structure from the map return value.
"""


my_list = [1, 2, 3, 4]

r = map(str, my_list)
print(type(r))

# this is one way to use the return value of map
for x in r:
    print(x)

# this is a different way to use it
print(list(map(str, my_list)))
