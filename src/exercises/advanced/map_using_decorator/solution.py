"""
solution.py
"""


def add1(f):
    def inner(*args, **kw):
        return f(*args, **kw) + 1

    return inner


def make_a_list(f):
    def inner(*args, **_kw):
        #    return [f(x) for x in args]  # noqa: ERA001  teaching: kept in the comment for the reader
        return [f(x) for x in args]

    return inner


@make_a_list
def square(x):
    return x * x


print(square(3, 2, 1))
