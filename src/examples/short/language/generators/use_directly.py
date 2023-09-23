"""
This is an example for how to use a generator directly and get all of its values
through the python API and not through the iterator abstraction (for loop).

Note that the following are equivalent:
- element = next(generator)
- element = generator.__next__()
- element = generator.send(None)
We use the first 1 (most simple) in the example.
"""

g = (x ** 2 for x in range(5))

while True:
    try:
        x = next(g)
        print(x)
    except StopIteration:
        g.close()
        break
