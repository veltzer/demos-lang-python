"""
This example shows that you cannot overload functions in python.
The second function 'overwrites' the first.

There is a kind of overloading in python using named arguments and
variable arguments but not of this kind.

Functions also share the same namespace with regular variables. So,
in this example,defining a variable named 'foo' would override the
function so that it cannot be used.
"""


def foo():
    print('hello')


def foo(a):
    print('hello', a)


try:
    # noinspection PyArgumentList
    foo()
except TypeError:
    print('oops,got an error')
foo('mark')
