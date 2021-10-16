"""
This example shows that you cannot overload functions in python.
The second function 'overwrites' the first.

There is a kind of overloading in python using named arguments and
variable arguments but not of this kind.

Functions also share the same namespace with regular variables. So,
in this example,defining a variable named 'foo' would override the
function so that it cannot be used.
"""


def demo_foo():
    print("hello")


# noinspection PyRedeclaration
# pylint: disable=function-redefined
def demo_foo(a):  # noqa: F811
    print(f"hello {a}")


try:
    # noinspection PyArgumentList
    # pylint: disable=no-value-for-parameter
    demo_foo()
except TypeError:
    print("oops, got an error")
demo_foo("mark")
