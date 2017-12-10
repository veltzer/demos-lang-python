#!/usr/bin/env python

"""
This example shows how to take an iterator and chunk it.
This means produce iterators that will ultimately cover
all of the data coming out of that iterator with each
one producing no more than N pieces of data.
"""

import itertools
import types
import timeit

def splice_groupby(data, n):
    return ((d for _, d in dd) for (_, dd) in itertools.groupby(enumerate(data), key=lambda v: v[0] // n))

def splice_groupby_closure(data, n):
    counter=[-1,0]
    def group_classifier(__):
        counter[0]+=1
        if counter[0]==n:
            counter[0]=0
            counter[1]+=1
        return counter[1]
    return (dd for (_, dd) in itertools.groupby(data, key=group_classifier))

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

for d in splice_groupby_closure(range(100), 7):
    #print(type(d))
    #assert isinstance(d, types.GeneratorType)
    print(list(d))

# lets compare the performance
def func_splice_groupby():
    for d in splice_groupby(range(1000000), 1000):
        _ = list(d)
def func_splice_simple():
    for d in splice_simple(range(1000000), 1000):
        _ = list(d)
def func_splice_groupby_closure():
    for d in splice_groupby_closure(range(1000000), 1000):
        _ = list(d)

print(timeit.timeit(func_splice_groupby, number=10))
print(timeit.timeit(func_splice_simple, number=10))
print(timeit.timeit(func_splice_groupby_closure, number=10))
