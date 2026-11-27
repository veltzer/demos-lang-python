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

    def set_price(self, newprice):
        self.__price = newprice

    def get_num_books(self=None):  # pyrefly: ignore[bad-function-definition]  teaching: self=None lets the method be called without an instance
        return Book.num


# lets create some books...
b1 = Book(14)
b2 = Book(13)
# lets output the static data in various ways...
print(Book.num)
print(b1.get_num_books())
print(Book.get_num_books(b1))
# these will throw an exception since you must pass an instance...
# print(Book.get_num_books())  # noqa: ERA001  teaching: kept in the comment for the reader
# print(Book.get_num_books(None))  # noqa: ERA001  teaching: kept in the comment for the reader
