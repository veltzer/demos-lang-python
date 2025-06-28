"""
solution
"""


def yield_some_stuff():
    """ yield some data """
    # pylint: disable=use-yield-from
    yield from range(5, 25, 5)


for i in yield_some_stuff():
    print(i)
