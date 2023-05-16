"""
This shows that "staticmethod" can be used by inheriting
classes as well. It works!
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


b1 = Book(14)
b2 = Book(13)

print(Book.num)
print(b1.getNumBooks())
print(Book.getNumBooks())


class FictionBook(Book):
    pass


b3 = FictionBook(15)
print(Book.num)
print(FictionBook.num)
print(Book.getNumBooks())
print(FictionBook.getNumBooks())
