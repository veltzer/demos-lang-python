"""
This example explores how best to concatenate strings in python.

The results are surprising.
- It seems the + operator is the quickest
- Join and %s%s come next.
- Formatting is last.

References:
- http://blog.lerner.co.il/speedy-string-concatenation-python/
"""

import timeit

x = 'abc'
y = 'def'


function_names = {}


def concat1():
    z = x + y
    return z


function_names[concat1] = '+ operator'


def concat2():
    # pylint: disable=consider-using-f-string
    z = '%s%s' % (x, y)
    return z


function_names[concat2] = '%s%s'


def concat3():
    # pylint: disable=consider-using-f-string
    z = '{}{}'.format(x, y)
    return z


function_names[concat3] = '{}{}'


def concat4():
    # pylint: disable=consider-using-f-string
    z = '{0}{1}'.format(x, y)
    return z


function_names[concat4] = '{0}{1}'


def concat5():
    return ''.join([x, y])


function_names[concat4] = 'join'


def concat6():
    return f"{x}{y}"


function_names[concat6] = 'f-string'


functions = [
    concat1,
    concat2,
    concat3,
    concat4,
    concat5,
    concat6,
]

number = 2000000

results = [(timeit.timeit(f, number=number), function_names[f]) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print(f"{r[0]:.4f}: {r[1]}")
