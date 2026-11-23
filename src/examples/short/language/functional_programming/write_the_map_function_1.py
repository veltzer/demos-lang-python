"""
this is an example of how the "map" function in python works
this is a naive implementation. the python implementation is coded
in C and is a lot faster than this one...
"""


def my_map(func, val_list):
    return [func(value) for value in val_list]


def square(x):
    return x * x


print(my_map(square, range(2, 8)))
