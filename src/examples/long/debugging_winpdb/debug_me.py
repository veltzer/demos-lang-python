""" debug_me.py """

import contextlib
from typing import Any


def simple_func(x: Any):
    x += 1

    # s = range(20)  # noqa: ERA001  teaching: kept in the comment for the reader
    # z = None  # noqa: ERA001  teaching: kept in the comment for the reader
    # w = ()  # noqa: ERA001  teaching: kept in the comment for the reader

    # y = dict((i, i ** 2) for i in s)  # noqa: ERA001  teaching: kept in the comment for the reader

    # k = set(range(5, 99))  # noqa: ERA001  teaching: kept in the comment for the reader

    with contextlib.suppress(AttributeError):
        _ = x.invalid

    # import sys  # noqa: ERA001  teaching: kept in the comment for the reader
    # sys.exit(1)  # noqa: ERA001  teaching: kept in the comment for the reader

    return 2 * x


def fermat(n: int):
    """Returns triplets of the form x^n+y^n=z^n.
    Warning! Untested with n>2.
    """
    for x in range(100):
        for y in range(1, x + 1):
            for z in range(1, x ** n + y ** n + 1):
                # from pudb import set_trace; set_trace()  # noqa: ERA001  teaching: kept in the comment for the reader
                if x ** n + y ** n == z ** n:
                    yield x, y, z


def main() -> None:
    # noinspection PyTypeChecker
    print("SF", simple_func(10))

    for i in fermat(2):
        print(i)

    print("FINISHED")


if __name__ == "__main__":
    main()
