"""
This method shows the types of regular methods vs the types of real static methods.
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

    @staticmethod
    def getNumBooks():
        return Book.num

    @classmethod
    def getNumBooks2(cls):
        return cls.num


b = Book(15)
print(Book.getNumBooks())
print(Book.getNumBooks2())

print(b.printit, type(b.printit))
print(Book.printit, type(Book.printit))
print(Book.getNumBooks, type(Book.getNumBooks))
print(Book.getNumBooks2, type(Book.getNumBooks2))
