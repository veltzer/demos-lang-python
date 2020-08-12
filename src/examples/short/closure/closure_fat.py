"""
This is an example of how to create a closure which is 'fat': meaning
has lots of data and not just primitives. In this case the closure
contains the list 'l' which can be very long indeed.
"""


def create_func(l):
    def inner_func(x):
        l.append(x)
        print(sum(l))

    return inner_func


inner = create_func([1, 2, 3])
inner(4)
inner(5)
inner(6)
