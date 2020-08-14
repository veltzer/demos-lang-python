"""
this is a simple solution to the reverse hash function exercise
"""


def rev_hash(o):
    return dict(map(lambda t: (t[1], t[0]), o.items()))


orig = {'Israel': 'Jerusalem', 'France':
    'Paris', 'Italy': 'Rome', 'Egypt': 'Cairo'}
rev = rev_hash(orig)
print(rev)
