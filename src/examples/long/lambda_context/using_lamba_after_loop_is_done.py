"""
This example shows why you should be careful with lambda contexts.

Lets explain when this happens:
- you define a lambda inside a loop
- the lambda references the loop variable or anything which is calculatd in
    loop and changes from iteration to iteration.
- you store the lambda reference so that it can be used after the loop is over.
- you use the lambda after the loop is over.

Why does the problem occur?
- Because the lambda definition DOES NOT make a copy of every variable used in it
and stores it with the reference.
- Actually, only one lambda is created
- So which value does it use when called?
    Which ever value the variable has AT THE TIME THAT IT IS CALLED.
    Inside the loop it's ok since the variable has the current value.
    Outside the loop this causes problems since it will refer to the last value
    of the variable

What does not solve this?
- turning the lambda to a function does not work.
- using partial but without arguments.

What does solve this?
- using a default value which is different every time. This is because
    values for parameters with defaults ARE stored with the function reference.
- using a function creator
- using partial.

References:
- https://github.com/PyCQA/pylint/issues/3107
"""

from functools import partial


def basic():
    """ This is the basic example. What does this produce? """
    handlers = []
    for i in range(10):
        # pylint: disable=cell-var-from-loop
        handlers.append(lambda: i)
    print([h() for h in handlers])


def wrong():
    """ This does not work since there will be only one f """
    handlers = []
    for i in range(10):
        def f():
            # pylint: disable=cell-var-from-loop
            return i
        handlers.append(f)
    print([h() for h in handlers])


def correction():
    """ This works because each f will be stored with it's own default value for 'val'. """
    handlers = []
    for i in range(10):
        def f(val=i):
            return val
        handlers.append(f)
    print([h() for h in handlers])


def creator_pattern():
    """ This is called a function creator pattern, it uses the closure of the function to store i. """
    def create_f(i):
        def f():
            return i
        return f
    handlers = []
    for i in range(10):
        handlers.append(create_f(i))
    print([h() for h in handlers])


def partial_pattern_wrong():
    """ This is using the partial python standard function, but without arguments it does not work """
    handlers = []
    for i in range(10):
        # pylint: disable=cell-var-from-loop,unnecessary-lambda-assignment
        f = lambda: i  # noqa: E731
        good_f = partial(f)
        handlers.append(good_f)
    print([h() for h in handlers])


def partial_pattern():
    """ This is using the partial python standard function """
    handlers = []
    for i in range(10):
        # pylint: disable=unnecessary-lambda-assignment
        f = lambda i: i  # noqa: E731
        good_f = partial(f, i)
        handlers.append(good_f)
    print([h() for h in handlers])


basic()
wrong()
correction()
creator_pattern()
partial_pattern_wrong()
partial_pattern()
