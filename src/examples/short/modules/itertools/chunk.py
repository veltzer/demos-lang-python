"""
This example shows how to take an iterator and chunk it.
This means produce iterators that will ultimately cover
all of the data coming out of that iterator with each
one producing N pieces of data (except possibly the last one).

The result is that the best option is to use the iterator
API directly (look at the function "chunk" below).

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

# lets compare the performance
range_limit = 1000000
jump = 7


def chunk_groupby(data, n):
    return ((d for _, d in dd) for _, dd in itertools.groupby(enumerate(data), key=lambda v: v[0] // n))


def chunk_groupby_closure(data, n):
    counter = [-1, 0]

    def group_classifier(__):
        counter[0] += 1
        if counter[0] == n:
            counter[0] = 0
            counter[1] += 1
        return counter[1]

    return (dd for _, dd in itertools.groupby(data, key=group_classifier))


def chunk_python(data, n):
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
                yield next(i)
            except StopIteration:
                over.cancel()
                return
                # raise e

    while not over.is_cancelled:
        yield return_n()


def chunk_itertools(data, n):
    i = iter(data)
    while True:
        # first = next(i)
        # second version is faster...
        # yield itertools.islice(itertools.chain((first,), i), n)
        # pylint: disable=stop-iteration-return
        yield itertools.chain((next(i),), itertools.islice(i, n - 1))


def chunk_generator(data, n):
    it = iter(data)
    return (itertools.chain((i,), itertools.islice(it, n - 1)) for i in it)


def func_chunk_groupby():
    for d in chunk_groupby(range(range_limit), jump):
        _ = list(d)


def func_chunk_groupby_closure():
    for d in chunk_groupby_closure(range(range_limit), jump):
        _ = list(d)


def func_chunk_python():
    for d in chunk_python(range(range_limit), jump):
        _ = list(d)


def func_chunk_itertools():
    for d in chunk_itertools(range(range_limit), jump):
        _ = list(d)


def func_chunk_generator():
    for d in chunk_generator(range(range_limit), jump):
        _ = list(d)


def main():
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
    for d in chunk_python(range(range_limit), jump):
        inspect.isgeneratorfunction(d)
        assert list(d) == list(range(count, min(count + jump, range_limit)))
        count += jump

    count = 0
    for d in chunk_itertools(range(range_limit), jump):
        inspect.isgeneratorfunction(d)
        assert list(d) == list(range(count, min(count + jump, range_limit))), "ld + lb"
        count += jump

    count = 0
    for d in chunk_generator(range(range_limit), jump):
        inspect.isgeneratorfunction(d)
        assert list(d) == list(range(count, min(count + jump, range_limit))), "ld + lb"
        count += jump

    how_much = 10
    print(f"groupby [{timeit.timeit(func_chunk_groupby, number=how_much)}]")
    print(f"groupby_closure [{timeit.timeit(func_chunk_groupby_closure, number=how_much)}]")
    print(f"python [{timeit.timeit(func_chunk_python, number=how_much)}]")
    print(f"itertools [{timeit.timeit(func_chunk_itertools, number=how_much)}]")
    print(f"generator [{timeit.timeit(func_chunk_generator, number=how_much)}]")


if __name__ == "__main__":
    main()
