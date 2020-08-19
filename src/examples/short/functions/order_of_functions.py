"""
    This example shows that a function in python can use a 'forward'
    defined function as long as the function in question is defined
    by the time the original function is called.

    Conclusion: in Python define all of your function at the beginning
    of your module in any order you like and only then put execution
    code. Then you don't have to worry about order at all.
"""


def f():
    g()


def g():
    print('hello')


f()
