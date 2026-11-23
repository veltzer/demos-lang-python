"""
This is the right way to create a static method in python.
Decorate it with the builtin "staticmethod" decorator function.
You can then call the method using the instance AND using
the class.
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


b1 = Book(14)
b2 = Book(13)

print(Book.num)
print(b1.get_num_books())
print(Book.get_num_books())
