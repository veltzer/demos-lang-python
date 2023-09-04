"""
this is a simple solution to the reverse hash function exercise
"""
import doctest


def rev_hash(o):
    """ reverse a hash (build a value=>key mapping)

    >>> rev_hash({"Israel":"Jerusalem","France":"Paris","Italy":"Rome","Egypt":"Cairo"})
    {'Jerusalem': 'Israel', 'Paris': 'France', 'Rome': 'Italy', 'Cairo': 'Egypt'}
    """
    ret = {}
    for k, v in o.items():
        ret[v] = k
    return ret


doctest.testmod()
