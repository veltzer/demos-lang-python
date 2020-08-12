"""
This example shows d.popitem()

The main point is that this method is atomic and can be used
to distribute values of a dictionary between threads or processess
in a multi-threaded or multi-processed pythong application.
"""

d = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
}
while d:
    key, value = d.popitem()
    print(key, '-->', value)
