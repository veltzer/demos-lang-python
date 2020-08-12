"""
lambda and apply again...
"""


def my_apply(f, seq):
    for x in seq:
        f(x)


def reverse_hash(d):
    target = {}
    my_apply(lambda k: target.__setitem__(d[k], k), d)
    # this will create a compilation error
    # my_apply(lambda k: target[d[k]]=k,orig)
    return target


orig = {'Israel': 'Jerusalem', 'France':
    'Paris', 'Italy': 'Rome', 'Egypt': 'Cairo'}
print(reverse_hash(orig))
