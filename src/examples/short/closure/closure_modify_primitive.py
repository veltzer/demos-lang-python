"""
This is an example that shows that you cannot change primitives in closures.
"""


def make_adder():
    # noinspection PyUnusedLocal
    # pylint: disable=unused-variable
    x = 0

    def adder():
        # noinspection PyUnboundLocalVariable,PyUnresolvedReferences
        # pylint: disable=undefined-variable
        x += 1  # noqa: F823
        # noinspection PyUnresolvedReferences
        print(x)

    return adder


f = make_adder()
f()
f()
f()
