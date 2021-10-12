"""
This example shows how you can manipulate via sys._getframe any stack
frame including your own
"""

import sys

# define a new local variable 'foo' and assign the value '42' to it...
# noinspection PyProtectedMember
sys._getframe().f_locals['foo'] = 42
print(foo)  # noqa: F821


def f():
    x = ['one']
    print('val before is {0}'.format(x[0]))
    g()
    print('val after is {0}'.format(x[0]))


def g():
    # noinspection PyProtectedMember
    sys._getframe(1).f_locals['x'][0] = 42


f()
