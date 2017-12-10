#!/usr/bin/env python

"""
This example shows how to take an iterator and chunk it.
This means produce iterators that will ultimately cover
all of the data coming out of that iterator with each
one producing no more than N pieces of data.
"""

from itertools import groupby, islice
import types

def splice_groupby(data, n):
    return ((d for _, d in dd) for (_, dd) in groupby(enumerate(data), key=lambda v: v[0] // n))

def splice_simple(data, n):
    class CancellationToken:
        def __init__(self):
            self.is_cancelled = False
        def cancel(self):
            self.is_cancelled = True
    i = iter(data)
    over = CancellationToken()
    def return_n():
        for _ in range(n):
            try:
                yield(next(i))
            except StopIteration as e:
                over.cancel()
                raise e
    while not over.is_cancelled:
        yield return_n()

for d in splice_groupby(range(100), 7):
    assert isinstance(d, types.GeneratorType)
    print(list(d))

for d in splice_simple(range(100), 7):
    assert isinstance(d, types.GeneratorType)
    print(list(d))
