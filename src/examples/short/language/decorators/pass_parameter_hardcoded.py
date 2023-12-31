"""
This is an example of how to pass parameters to a decorator.
"""


def multply_by(n):
    def decorator_func(func):
        def inner(a, b):
            return func(a, b) * n
        return inner
    return decorator_func


@multply_by(n=5)
def add(a, b):
    return a + b


print(f"did you know that 2+2={add(2,2)}")
