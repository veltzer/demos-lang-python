"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""


def decor(func):
    def inner():
        print(f"decor start {func.__name__}")
        return_value = func()
        print(f"decor end {func.__name__}")
        return return_value

    return inner


@decor
def demo_bar():
    print("in demo_bar")


@decor
def demo_foo():
    print("in demo_foo start")
    demo_bar()
    print("in demo_foo end")


demo_foo()
