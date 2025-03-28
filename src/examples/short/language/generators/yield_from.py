""" yield_from.py """


def yield_some():
    yield 1
    yield 2


def yield_more():
    yield 3
    yield 4


def yield_both():
    yield from yield_some()
    yield from yield_more()


for x in yield_both():
    print(x)
