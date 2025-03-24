"""
Solution10
"""


def apply_funcs(funcs, x):
    return (f(x) for f in funcs)


# this does not work (prints "generator something"...)
print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
# this is the way to get the data out of the generator...
for v in apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5):
    print(v)
