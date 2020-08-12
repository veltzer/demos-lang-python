"""
"""


class Book(object):
    """ initializer """

    def __init__(self, price):
        self.price = price

    def printMe(self):
        print('price is', self.price)


''' Lets show how we use our object... '''
b = Book(50)
b.printMe()

m = b.printMe
m()
print(type(m))


def myfunc(self):
    print('in myfunc', self)


b.newmethod = myfunc
print(type(b.newmethod))
b.newmethod()  # -> newmethod(b)

# this fails
try:
    b.newmethod = myfunc
    print(type(b.newmethod))
    b.newmethod(b)
except:
    print('all is well, got exception')

Book.newmethod = myfunc
b.newmethod()

try:
    b.printMe = myfunc
    b.printMe()
except:
    print('all is well, got exception')
