"""
This example explores how best to catenate strings in python.

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


def concat1():
    z = x + y
    return z


concat1.name = '+ operator'


def concat2():
    z = '%s%s' % (x, y)
    return z


concat2.name = '%s%s'


def concat3():
    z = '{}{}'.format(x, y)
    return z


concat3.name = '{}{}'


def concat4():
    z = '{0}{1}'.format(x, y)
    return z


concat4.name = '{0}{1}'


def concat5():
    return ''.join([x, y])


concat5.name = 'join'

functions = [
    concat1,
    concat2,
    concat3,
    concat4,
    concat5,
]

number = 2000000

results = [(timeit.timeit(f, number=number), f.name) for f in functions]
sorted_results = sorted(results, key=lambda tup: tup[0])
for r in sorted_results:
    print('{0:.4f}: {1}'.format(r[0], r[1]))
