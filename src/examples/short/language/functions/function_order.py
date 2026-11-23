"""
This example explores correct function order in the source code.

This means that a function cannot be used until after it has been defined.
"""

# this is wrong since foo is not defined
# noinspection PyBroadException
try:
    # noinspection PyUnboundLocalVariable
    demo_foo()  # pyrefly: ignore[unbound-name]  teaching: shows that a name must be defined before the call that uses it runs
except NameError:
    print("yep, this failed")


def demo_foo():
    print("this is demo_foo")
    demo_bar()  # noqa: F821  teaching: demo_bar is called before it is defined


# this will call foo but will fail once foo tried to call bar
# noinspection PyBroadException
try:
    demo_foo()
except NameError:
    print("yep, this failed")


def demo_bar():
    print("this is bar")


# this should work now that both "foo" and "bar" are defined
demo_foo()

del demo_bar

# now that "bar" is no longer defined any call to "foo" should fail
try:
    demo_foo()
except NameError:
    print("yep, this failed")
