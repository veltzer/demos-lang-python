# type: ignore
"""
This example shows how you can manipulate via sys._getframe any stack
frame including your own
"""

import sys

# define a new local variable "foo" and assign the value "42" to it...
# noinspection PyProtectedMember
# pylint: disable=protected-access
sys._getframe().f_locals["foo"] = 42
# pylint: disable=undefined-variable
print(foo)  # noqa: F821


def f():
    x = ["one"]
    print(f"val before is {x[0]}")
    g()
    print(f"val after is {x[0]}")


def g():
    # noinspection PyProtectedMember
    # pylint: disable=protected-access
    sys._getframe(1).f_locals["x"][0] = 42


f()
