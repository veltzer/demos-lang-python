"""
this is a simple solution to the reverse dict function exercise
"""
import doctest


def rev_dict(d):
    """ reverse a dict (build a value=>key mapping)

    >>> rev_dict({"Israel":"Jerusalem","France":"Paris","Italy":"Rome","Egypt":"Cairo"})
    {"Jerusalem": "Israel", "Paris": "France", "Rome": "Italy", "Cairo": "Egypt"}
    """
    rev_d = {}
    for k, v in d.items():
        rev_d[v] = k
    return rev_d


doctest.testmod()
