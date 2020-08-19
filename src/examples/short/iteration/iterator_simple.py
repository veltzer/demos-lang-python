"""
this is an example of building your own iterator
In this example the object returns itself as the iterator
(the return value from the __iter__ function). But it could have
chosen to return another object.

Differences between python2.7 and python3:
- in python2.7 the __next__ method should be called 'next'.
"""

'''Iterator for looping over a sequence backwards'''


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def main():
    # And now lets use the iterator...
    y = [1, 2, 3, 4, 5, 6, 7]
    for x in Reverse(y):
        print(x)


main()
