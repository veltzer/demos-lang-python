"""
This solution uses lamba and apply (advanced stuff)
"""


def my_apply(function, seq):
    """ apply a function on a sequence """
    for item in seq:
        function(item)


orig = {
    'Israel': 'Jerusalem',
    'France': 'Paris',
    'Italy': 'Rome',
    'Egypt': 'Cairo',
}
target = {}
# pylint: disable=unnecessary-dunder-call
u = map(lambda k: target.__setitem__(orig[k], k), orig)
# u is unused
print(target)
tg2 = {}
my_apply(lambda k: tg2.__setitem__(orig[k], k), orig)
print(tg2)
