"""
This example shows that when "map" is given a generator it DOES NOT create a list
with all the elements that the generator provides but rather creates a new generator
that will provide you with the processed data, one element at a time.

You can see that all the prints are interleaved which proves that the elements are generated
one at a time.
"""


def my_gen():
    for i in range(10):
        print("my_gen")
        yield i ** 2


def plus1(t):
    print("plus1")
    return t + 1


for x in map(plus1, my_gen()):
    print(x)
