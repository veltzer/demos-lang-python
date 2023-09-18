"""
this is an example of building your own iterator
In this example the object returns itself as the iterator
(the return value from the __iter__ function). But it could have
chosen to return another object.
"""


class Reverse:
    """ Iterator for looping over a sequence backwards """
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
    for x in Reverse(range(10)):
        print(x)
    print(type(Reverse))
    print(Reverse("foo"))


main()
