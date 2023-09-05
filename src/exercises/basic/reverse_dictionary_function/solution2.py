"""
this is a simple solution to the reverse dict function exercise
"""


def rev_dict(d):
    rev_d = {}
    # pylint: disable=unnecessary-dunder-call
    for _ in map(lambda t: rev_d.__setitem__(t[1], t[0]), d.items()):
        pass
    # the next version does not work because lambda does not support assignment
    # for _ in map(lambda t: rev_d[t[1]]=t[0], d.items())
    #     pass
    return rev_d


orig = {
    "Israel": "Jerusalem",
    "France": "Paris",
    "Italy": "Rome",
    "Egypt": "Cairo",
}
rev = rev_dict(orig)
print(rev)
