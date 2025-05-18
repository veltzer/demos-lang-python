"""
This is the most simple python iterator similar to range(min, max)
"""


class MyRange:
    """ Iterator line range """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        if self.a == self.b:
            raise StopIteration
        return_value = self.a
        self.a = self.a + 1
        return return_value


def main():
    # And now lets use the iterator...
    for x in MyRange(10,20):
        print(x)


main()
