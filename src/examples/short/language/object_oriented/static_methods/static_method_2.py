"""
A nicer version
"""


class Book:
    num = 0

    def __init__(self, price):
        self.__price = price
        Book.num += 1

    def printit(self):
        print("price is", self.__price)

    def setPrice(self, newprice):
        self.__price = newprice

    def getNumBooks(self=None):
        return Book.num


# lets create some books...
b1 = Book(14)
b2 = Book(13)
# lets output the static data in various ways...
print(Book.num)
print(b1.getNumBooks())  # type: ignore
print(Book.getNumBooks(b1))
# these will throw an exception since you must pass an instance...
# print(Book.getNumBooks())
# print(Book.getNumBooks(None))
