"""
Demonstrate "object orientation" via a mutated default argument:
the ``items=[]`` list is created once, at function definition time, and is
shared across all calls - so it behaves like a piece of object state.

This is a classic Python gotcha, so the pylint warnings about it are silenced
on purpose.
"""


# pylint: disable=dangerous-default-value,inconsistent-return-statements,unused-argument
def op(o, x=None, items=[], s=set()):       # the [] is created once, at def time  # noqa: B006
    if o == "push":
        items.append(x)
        return None
    if o == "pop":
        return items.pop()


op("push", 2)
op("push", 3)
op("push", 4)
print(op("pop"))
print(op("pop"))
op("push", 5)
