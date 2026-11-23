"""
Solution6
"""


def apply_funcs(funcs, x):
    """Apply a list of unary functions on an argument,
    Return the result"""
    return map(lambda f: f(x), funcs)  # noqa: C417  teaching: demonstrating map with a lambda


print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
