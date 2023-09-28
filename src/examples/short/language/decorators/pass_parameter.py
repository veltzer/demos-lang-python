"""
This is an example of how to pass parameters to a decorator.
"""


def multply_by(func, n):
    def inner(*arg, **kwargs):
        return func(*arg, **kwargs) * n
    return inner


def add(a, b):
    return a + b


add = multply_by(add, 5)
print(f"did you know that 2+2={add(2,2)}")
