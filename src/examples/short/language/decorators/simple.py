"""
This is a simple example of writing a python function decorator

References:
- https://pythonconquerstheuniverse.wordpress.com/2009/08/06/introduction-to-python-decorators-part-1/
"""


def run_it_3_times(func):
    def inner():
        func()
        func()
        func()
    return inner


@run_it_3_times
def hello():
    print("hello")


hello()
