"""
This is an example that shows that you cannot change primitives in closures.
"""


def make_adder():
    # noinspection PyUnusedLocal
    x = 0

    def adder():
        # noinspection PyUnboundLocalVariable,PyUnresolvedReferences
        x += 1  # noqa: F823
        # noinspection PyUnresolvedReferences
        print(x)

    return adder


f = make_adder()
f()
f()
f()
