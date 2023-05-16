"""
This is an example of how to create a closure which is "fat": meaning
has lots of data and not just primitives. In this case the closure
contains the list "function_list" which can be very long indeed.
"""


def create_func(function_list):
    def inner_func(x):
        function_list.append(x)
        print(sum(function_list))

    return inner_func


inner = create_func([1, 2, 3])
inner(4)
inner(5)
inner(6)
