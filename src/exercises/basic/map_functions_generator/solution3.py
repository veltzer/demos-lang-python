"""
this is a function accepting a list of unary functions and an argument
the function returns a list where each element is the application of the
relevant unary function on the single argument
"""


def map_like(func_list, *extra, **named_extra):
    result = []
    for func in func_list:
        result.append(func(*extra, **named_extra))
    return result


def add(x, y, _correction_factor=7):
    return x + y


def mul(x, y, correction_factor=7):
    return x * y - correction_factor


def sub(x, y, _correction_factor=7):
    return x - y


print(map_like([add, mul, sub], 7, 3, correction_factor=2))
