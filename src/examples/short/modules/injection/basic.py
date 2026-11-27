"""
This is a demo of using the inject framework for python which is
a dependency injection framework.

References:
- https://pypi.python.org/pypi/Inject

TODO:
- show how to inject by name instead of by type.
"""

from typing import Any

import inject


@inject.params(var=list)
def doit(a: int, b: int, var: Any) -> None:
    print(a, b, var)


def my_config(binder: inject.Binder) -> None:
    binder.bind(list, [1, 2, 3])


inject.configure(config=my_config)


def f1() -> None:
    f2()


def f2() -> None:
    f3()


def f3() -> None:
    doit(a=5, b=7)


f1()
