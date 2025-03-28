"""
Solution1
"""


def apply_funcs(funcs, x):
    """Apply a list of unary functions on an argument,
    Return the result"""
    return map(lambda f: f(x), funcs)
