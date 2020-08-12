"""
This is a solution with a generator...
"""


def apply_funcs(funcs, x):
    """ a different version with an iteration """
    for f in funcs:
        print('in the function, going to yield {0}'.format(f(x)))
        yield f(x)


# this does not work (prints 'generator something'...)
print(apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5))
for v in apply_funcs([lambda x: x ** 2, lambda x: x + 1], 5):
    print('in the for loop, going to output {0}'.format(v))
    print(v)
