"""
Excercise: write a function to inverse a dictionary.
Assume that all values are different.
"""
import doctest
from typing import Any


def rev_dict1(d: Any):
    """
    >>> rev_dict1({"a": 2, "b": 3})=={2: "a", 3: "b"}
    True
    """
    return {v: k for k, v in d.items()}


def rev_dict2(d: Any):
    """
    >>> rev_dict2({"a": 2, "b": 3})=={2: "a", 3: "b"}
    True
    """
    # recall that zip(d.keys(), d.values())==d.items()
    return dict(zip(d.values(), d.keys(), strict=False))


def rev_dict3(d: Any):
    """
    >>> rev_dict3({"a": 2, "b": 3})=={2: "a", 3: "b"}
    True
    """
    # list comprehension
    return {v: k for k, v in d.items()}


def rev_dict4(d: Any):
    """
    >>> rev_dict4({"a": 2, "b": 3})=={2: "a", 3: "b"}
    True
    """
    # generator expression (same but no intermediate list)
    return {v: k for k, v in d.items()}


def rev_dict5(d: Any):
    """
    >>> rev_dict5({"a": 2, "b": 3})=={2: "a", 3: "b"}
    True
    """
    # dictionary comprehension
    return {v: k for k, v in d.items()}


doctest.testmod()
