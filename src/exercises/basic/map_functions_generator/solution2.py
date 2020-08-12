"""
this is a function accepting a list of unary functions and an argument
the function returns a list where each element is the application of the
relevant unary function on the single argument
"""


def map_like(func_list, arg):
    result = []
    for func in func_list:
        result.append(func(arg))
    return result


def square(x):
    return x * x


def triple(x):
    return x * 3


def plusone(x):
    return x + 1


print(map_like([square, triple, plusone], 7))
