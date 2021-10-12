"""
Using a for loop
"""


import doctest


def apply_funcs1(funcs, x):
    """Apply a list of unary functions on an argument.

    Return a list of the results.

    >>> apply_funcs1([lambda x:x**2, lambda x:x+1], 3)
    [9, 4]
    """
    results = []
    for f in funcs:
        results.append(f(x))
    return results


def apply_funcs2(funcs, x):
    """Apply a list of unary functions on an argument.

    Return a list of the results.

    This is using list comprehensions

    >>> apply_funcs2([lambda x:x**2, lambda x:x+1], 3)
    [9, 4]
    """
    return [f(x) for f in funcs]


def apply_funcs3(funcs, x):
    """Apply a list of unary functions on an argument.

    Return a list of the results.

    This is using the builtin 'map' function.

    >>> apply_funcs3([lambda x:x**2, lambda x:x+1], 3)
    [9, 4]
    """
    # Note that we are mapping over the `funcs`, not over `x`.
    return map(lambda f: f(x), funcs)


# Bonus: With any number of arguments
# ===================================


def apply_funcs4(funcs, *args, **kw):
    """Apply a list of functions on the same arguments.

    Return a list of the results.

    >>> apply_funcs4([lambda x,y: x+y, lambda x,y: x*y], 3, y=4)
    [7, 12]
    """
    return [f(*args, **kw) for f in funcs]


doctest.testmod()
