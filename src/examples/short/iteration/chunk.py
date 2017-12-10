#!/usr/bin/env python

"""
This example shows how to take an iterator and chunk it.
This means produce iterators that will ultimately cover
all of the data coming out of that iterator with each
one producing N pieces of data (except possibly the last one).

The result is that the best option is to use the iterator
API directly (look at the function 'chunk' below).
"""

import itertools
import types
import timeit

def chunk_groupby(data, n):
    return ((d for _, d in dd) for (_, dd) in itertools.groupby(enumerate(data), key=lambda v: v[0] // n))

def chunk_groupby_closure(data, n):
    counter=[-1,0]
    def group_classifier(__):
        counter[0]+=1
        if counter[0]==n:
            counter[0]=0
            counter[1]+=1
        return counter[1]
    return (dd for (_, dd) in itertools.groupby(data, key=group_classifier))

def chunk(data, n):
    class __CancellationToken:
        def __init__(self):
            self.is_cancelled = False
        def cancel(self):
            self.is_cancelled = True
    i = iter(data)
    over = __CancellationToken()
    def return_n():
        for _ in range(n):
            try:
                yield(next(i))
            except StopIteration as e:
                over.cancel()
                raise e
    while not over.is_cancelled:
        yield return_n()

for d in chunk_groupby(range(100), 7):
    assert isinstance(d, types.GeneratorType)
    print(list(d))

for d in chunk_groupby_closure(range(100), 7):
    #print(type(d))
    #assert isinstance(d, types.GeneratorType)
    print(list(d))

for d in chunk(range(100), 7):
    assert isinstance(d, types.GeneratorType)
    print(list(d))

# lets compare the performance
def func_chunk_groupby():
    for d in chunk_groupby(range(1000000), 1000):
        _ = list(d)
def func_chunk_groupby_closure():
    for d in chunk_groupby_closure(range(1000000), 1000):
        _ = list(d)
def func_chunk():
    for d in chunk(range(1000000), 1000):
        _ = list(d)

print(timeit.timeit(func_chunk_groupby, number=10))
print(timeit.timeit(func_chunk_groupby_closure, number=10))
print(timeit.timeit(func_chunk, number=10))
