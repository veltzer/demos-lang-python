"""
This is a demo of using the inject framework for python which is
a dependency injection framework.

References:
- https://pypi.python.org/pypi/Inject

TODO:
- show how to inject by name instead of by type.
"""

import inject


@inject.params(var=list)
def doit(var):
    print(var)


def configure(binder: inject.Binder) -> None:
    binder.bind(list, [1, 2, 3])


inject.configure(config=configure)

# pylint: disable=no-value-for-parameter
doit()
