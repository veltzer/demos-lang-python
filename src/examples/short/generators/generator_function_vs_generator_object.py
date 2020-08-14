"""
This example shows the difference between a generator function and a
generator object.

generator function: a function which is a generator (has yields).
    - can be detected using inspect.isgeneratorfunction(f)
generator object: a generator function which has been called once.
    - can be detected using isinstance(f, types.GeneratorType)

References:
- https://stackoverflow.com/questions/6416538/how-to-check-if-an-object-is-a-generator-object-in-python
"""

import inspect
import types


def generator_function():
    yield 1
    yield 2
    yield 3


print(type(generator_function))
assert inspect.isgeneratorfunction(generator_function)
assert not isinstance(generator_function, types.GeneratorType)

f = generator_function()
print(type(f))
assert not inspect.isgeneratorfunction(f)
assert isinstance(f, types.GeneratorType)
