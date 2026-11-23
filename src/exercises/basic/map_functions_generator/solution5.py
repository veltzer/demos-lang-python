"""
Naive version of a solution, just construct a list...
No generators here.
"""


def apply_funcs(funcs, x):
    """ a different version with an iteration """
    return [f(x) for f in funcs]


print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
