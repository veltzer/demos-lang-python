"""
This example shows how to stop a generator using the return value
of the generator function
"""


def generate():
    for i in range(10):
        if i == 5:
            print("yielding False")
            yield False
        print("yielding True")
        yield True


print(all(generate()))
