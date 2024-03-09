"""
solution
"""


def yield_some_stuff():
    """ yield some data """
    # pylint: disable=use-yield-from
    for data in range(5, 25, 5):
        yield data


for i in yield_some_stuff():
    print(i)
