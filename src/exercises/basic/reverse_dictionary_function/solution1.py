"""
this is a simple solution to the reverse dict function exercise
"""
import doctest
from typing import Any


def rev_dict(d: Any):
    """ reverse a dict (build a value=>key mapping)

    >>> rev_dict({"Israel":"Jerusalem","France":"Paris","Italy":"Rome","Egypt":"Cairo"})
    {"Jerusalem": "Israel", "Paris": "France", "Rome": "Italy", "Cairo": "Egypt"}
    """
    return {v: k for k, v in d.items()}


doctest.testmod()
