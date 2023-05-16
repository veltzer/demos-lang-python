"""
this is an example of how the "map" function in python works
this is a naive implementation. the python implementation is coded
in C and is a lot faster than this one...
"""


def my_map(func, val_list):
    result = []
    for value in val_list:
        result.append(func(value))
    return result


def square(x):
    return x * x


print(my_map(square, range(2, 8)))
