"""
this is a simple solution to the reverse dict function exercise
"""


def rev_dict(d):
    return dict(map(lambda t: (t[1], t[0]), d.items()))  # noqa: C417  teaching: demonstrating map with a lambda


orig = {
    "Israel": "Jerusalem",
    "France": "Paris",
    "Italy": "Rome",
    "Egypt": "Cairo",
}
rev = rev_dict(orig)
print(rev)
