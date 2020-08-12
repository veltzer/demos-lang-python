"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""


def decor(func):
    def inner():
        print("decor start", func.__name__)
        return_value = func()
        print("decor end", func.__name__)
        return return_value

    return inner


@decor
def bar():
    print("in bar")


@decor
def foo():
    print("in foo start")
    bar()
    print("in foo end")


foo()
