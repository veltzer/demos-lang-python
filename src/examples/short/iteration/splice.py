#!/usr/bin/env python

"""
This example shows how to take an iterator and chunk it.
This means produce iterators that will ultimately cover
all of the data coming out of that iterator with each
one producing no more than N pieces of data.
"""

from itertools import groupby, islice
import types

def splice_them(data, n):
    return ((d for _, d in dd) for (_, dd) in groupby(enumerate(data), key=lambda v: v[0] // n))


def splice_simple(data, n):
    ''' this does not work '''
    r = islice(data, n)
    while r:
        yield r
        r = islice(data, n)

def splice_so_simple(data, n):
    ret = []
    i = data.__iter__()
    d = i.next()
    print(d)
    x = n
    while d and x >= 0:
        ret.append(d)
        d = next(i)
        x -= 1
    yield ret

for d in splice_them(range(100), 10):
    assert isinstance(d, types.GeneratorType)
    print(list(d))

for d in splice_so_simple(range(100), 10):
    print(type(d))
    # assert isinstance(d, types.GeneratorType)
    print(list(d))
