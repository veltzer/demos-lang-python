"""
This example shows that when map is given a generator it DOES NOT create a list
with all the elements that the generator provides but rather iterates the generator
added one element at a time to the resulting list.
"""


def my_gen():
    for i in range(10):
        print('my_gen')
        yield i ** 2


def plus1(x):
    print('plus1')
    return x + 1


map(plus1, my_gen())
