"""
This solution uses lamba and apply (advanced stuff)
"""


def my_apply(f, seq):
    for x in seq:
        f(x)


orig = {'Israel': 'Jerusalem', 'France':
    'Paris', 'Italy': 'Rome', 'Egypt': 'Cairo'}
target = {}
u = map(lambda k: target.__setitem__(orig[k], k), orig)
# u is unused
print(target)
tg2 = {}
my_apply(lambda k: tg2.__setitem__(orig[k], k), orig)
print(tg2)
