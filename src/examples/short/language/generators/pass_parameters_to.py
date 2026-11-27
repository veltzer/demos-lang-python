"""
This example shows that you can pass parameters to the generator
function...
"""


def generate_items(start: int, stop: int):
    yield from range(start, stop)


for x in generate_items(2, 6):
    print(x)
