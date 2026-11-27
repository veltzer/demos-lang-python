"""
This is a simple doctest example.
"""

import doctest


def triple(x: int):
    """ return x*3

    >>> triple(7)
    21
    """
    return x * 3


def square(x: int):
    """ return the square of x

    >>> square(7)
    49
    """
    # notice this bug...
    return x * x + 1


doctest.testmod()
