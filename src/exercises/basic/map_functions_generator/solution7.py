"""
Solution7
"""

def apply_funcs(funcs, x):
    """Apply a list of unary functions on an argument,
    Return the result"""
    return [f(x) for f in funcs]


print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
