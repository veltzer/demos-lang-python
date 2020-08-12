"""
This is an example of building an iterator. In this case the iterator
object returned is a different object than the one which is being iterated.
This is a nicer design.
"""


class RevIter:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


'''
Iterator for looping over a sequence backwards
'''


class Reverse:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return RevIter(self.data)


'''
And now lets use the iterator...
'''
for x in Reverse(range(7)):
    print(x)

'''
notice that Reverse(x) is NOT an iterator,at least by pythons understanding of it.
Compare to pythons own reversed(x) implementation which does return an iterator...
'''
l = range(7)
r1 = Reverse(l)
print(type(r1))
print('__next__' in dir(r1))
print('__iter__' in dir(r1))
r2 = reversed(l)
print(type(r2))
print('__next__' in dir(r2))
print('__iter__' in dir(r2))
