#!/usr/bin/env python

"""
This example shows how to take an iterator and chunk it.
This means produce iterators that will ultimately cover
all of the data coming out of that iterator with each
one producing N pieces of data (except possibly the last one).

The result is that the best option is to use the iterator
API directly (look at the function 'chunk' below).

Regarding checking if something is a generator.
There are two ways to check this:
- using types.GeneratorType:
    import types
    assert isinstance(x, types.GeneratorType)
- using inspect:
    import inspect
    inspect.isgeneratorfunction(x)
it seems that the second catches more than the second and that it
what we use here.
"""

import itertools
import timeit
import inspect

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

range_limit = 100
jump = 7
count = 0
for d in chunk_groupby(range(range_limit), jump):
    inspect.isgeneratorfunction(d)
    assert list(d) == list(range(count, min(count + jump, range_limit)))
    count += jump

count = 0
for d in chunk_groupby_closure(range(range_limit), jump):
    inspect.isgeneratorfunction(d)
    assert list(d) == list(range(count, min(count + jump, range_limit)))
    count += jump

count = 0
for d in chunk(range(range_limit), jump):
    inspect.isgeneratorfunction(d)
    assert list(d) == list(range(count, min(count + jump, range_limit)))
    count += jump

# lets compare the performance
range_limit = 1000000
jump = 1000
def func_chunk_groupby():
    for d in chunk_groupby(range(range_limit), jump):
        _ = list(d)
def func_chunk_groupby_closure():
    for d in chunk_groupby_closure(range(range_limit), jump):
        _ = list(d)
def func_chunk():
    for d in chunk(range(range_limit), jump):
        _ = list(d)

how_much = 10
print(timeit.timeit(func_chunk_groupby, number=how_much))
print(timeit.timeit(func_chunk_groupby_closure, number=how_much))
print(timeit.timeit(func_chunk, number=how_much))
