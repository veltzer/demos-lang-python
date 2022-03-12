"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""


def decor(_func):
    def inner():
        print("goodbye")
    return inner


@decor
def demo_bar():
    print("hello")


demo_bar()
