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

    def set_price(self, newprice):
        self.__price = newprice

    @staticmethod
    def get_num_books():
        return Book.num

    @classmethod
    def get_num_books2(cls):
        return cls.num


b = Book(15)
print(Book.get_num_books())
print(Book.get_num_books2())

print(b.printit, type(b.printit))
print(Book.printit, type(Book.printit))
print(Book.get_num_books, type(Book.get_num_books))
print(Book.get_num_books2, type(Book.get_num_books2))
