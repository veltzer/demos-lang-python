"""
This is a demo of how to override python builtins.
In general you can override builtins in python but then the question is
how do you call the original functions.

There are two ways to solve this:
- using the builtins built-in package.
- storing the old function pointer.
"""

import builtins


def my_max(*args):
    print("hey, I am here...")
    # now call the builtin "max" function
    return builtins.max(args)


print(my_max(1, 2))

original_min = min


def my_min(*args):
    print("hey, I am here...")
    # now call the builtin "min" function
    return original_min(args)


print(my_min(1, 2))
