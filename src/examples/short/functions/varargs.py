"""
This example shows how to use varargs in python to do useful work.
In this case, calling a function many times without knowing the function
or the arguments that it is supposed to receive.
"""


def call_many_times(func, times, *args, **kwargs):
    for x in range(times):
        func(*args, **kwargs)


call_many_times(print, 5, 'hello')
