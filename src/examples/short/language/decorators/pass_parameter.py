"""
This is an example of how to create a decorator which can receive
a parameter (n in this case).

Another things about this example is that we decorate "by hand"
without using the `@` python syntax.
"""


def multply_by(func, n):
    """
    The thing to understand about this decorator is that it can decorate
    any function because of the use of *arg, **kwargs and the return value
    """
    def inner(*arg, **kwargs):
        return func(*arg, **kwargs) * n
    return inner


def add(a, b):
    return a + b


def square(x):
    return x * x


add = multply_by(add, 5)
print(f"did you know that 2+2={add(2,2)}")
square = multply_by(square, 7)
print(f"did you know that 2*2={square(2)}")
