""" using a regular for loop with yield """


def apply_funcs_gen1(funcs, x):
    """Generate results of functions applied to an argument.
    >>> def print_a(x):
    ...     print('a')
    ...     return x
    >>> def print_b(x):
    ...     print('b')
    ...     return x
    >>> for res in apply_funcs_gen1([print_a, print_b], 42):
    ...     print(res)
    a
    42
    b
    42
    """
    for f in funcs:
        yield f(x)


''' using generator comprehensions '''


def apply_funcs_gen2(funcs, x):
    """Generate results of functions applied to an argument.
    >>> def print_a(x):
    ...     print('a')
    ...     return x
    >>> def print_b(x):
    ...     print('b')
    ...     return x
    >>> for res in apply_funcs_gen2([print_a, print_b], 42):
    ...     print(res)
    a
    42
    b
    42
    """
    return (f(x) for f in funcs)


import doctest

doctest.testmod()
