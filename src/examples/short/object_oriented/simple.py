"""
This is a fairly simple basic OO example

Notes:
- Python style is not to do getters and setters and use properties
later if need be (in most cases this is not needed).
- In python3 there is no need for Book to inherit from any base class.
It will get all the language support for object oriented programming
without this inheritance. If you do not inherit from any class then
you implicitly inherit from 'object'.
- In python2.7 you had to explicitly inherit from 'object' or else
you would not get the full object oriented support from the language.
- '__init__' is not really a constructor. You can throw exceptions from
it. You can leave it out entirely. You can break early from it. It
is really an initializer.
"""


class Book:
    def __init__(self, price):
        """ initializer """
        self.price = price

    def printMe(self):
        print('price is', self.price)


# Lets show how we use our object
b = Book(50)
b.printMe()
b.price = 60
b.printMe()
