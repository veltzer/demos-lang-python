"""
This example shows that you cannot overload functions in python.
The second function "overwrites" the first.

There is a kind of overloading in python using named arguments and
variable arguments but not of this kind.

Functions also share the same namespace with regular variables. So,
in this example,defining a variable named "foo" would override the
function so that it cannot be used.
"""



def demo_foo():
    print("hello")


# noinspection PyRedeclaration
def demo_foo(a):  # noqa: F811  teaching: the second definition deliberately replaces the first
    print(f"hello {a}")


try:
    # noinspection PyArgumentList
    demo_foo()  # pyrefly: ignore[missing-argument]  teaching: the second def replaced the one-argument version, so the call fails
except TypeError:
    print("oops, got an error")
demo_foo("mark")
