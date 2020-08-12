"""
this is a simple solution to the reverse hash function exercise
"""

def rev_hash(o):
    ret = {}
    map(lambda t: ret.__setitem__(t[1], t[0]), o.items())
    return ret


orig = {'Israel': 'Jerusalem', 'France':
    'Paris', 'Italy': 'Rome', 'Egypt': 'Cairo'}
rev = rev_hash(orig)
print(rev)
