"""
An even better implementation of map as a generator.
"""


def my_map(func, val_list):
    for value in val_list:
        yield func(value)


def square(x):
    return x * x


for x in my_map(square, range(2, 8)):
    print(x)
