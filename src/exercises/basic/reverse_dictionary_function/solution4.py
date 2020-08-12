"""
Excercise: write a function to inverse a dictionary.
Assume that all values are different.
"""


def rev_dict1(d):
    """
    >>> rev_dict1({'a': 2, 'b': 3})=={2: 'a', 3: 'b'}
    True
    """
    rev_d = {}
    for (k, v) in d.items():
        rev_d[v] = k
    return rev_d


def rev_dict2(d):
    """
    >>> rev_dict2({'a': 2, 'b': 3})=={2: 'a', 3: 'b'}
    True
    """
    # recall that zip(d.keys(), d.values())==d.items()
    return dict(zip(d.values(), d.keys()))


def rev_dict3(d):
    """
    >>> rev_dict3({'a': 2, 'b': 3})=={2: 'a', 3: 'b'}
    True
    """
    # list comprehension
    return dict([(v, k) for (k, v) in d.items()])


def rev_dict4(d):
    """
    >>> rev_dict4({'a': 2, 'b': 3})=={2: 'a', 3: 'b'}
    True
    """
    # generator expression (same but no intermediate list)
    return dict((v, k) for (k, v) in d.items())


def rev_dict5(d):
    """
    >>> rev_dict5({'a': 2, 'b': 3})=={2: 'a', 3: 'b'}
    True
    """
    # generator expression (same but no intermediate list)
    return {v: k for k, v in d.items()}


import doctest

doctest.testmod()
