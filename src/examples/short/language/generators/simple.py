"""
A simple example of a generator.

NOTES:
- note that the generator function can be infinite.
"""


def generate_items():
    yield from range(10)


for x in generate_items():
    print(x)
