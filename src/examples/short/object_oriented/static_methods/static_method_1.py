"""
This is a * sort * of static method but is ugly since the
function is really global and not in the class.
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


def getNumBooks():
    return Book.num


# lets create some books...
b1 = Book(14)
b2 = Book(13)

# lets access the static member and the static methods...
print(f"Book.num (direct access) is {Book.num}")
print(f"getNumBooks() is {getNumBooks()}")
try:
    print(b1.getNumBooks())  # type: ignore
except AttributeError:
    print("no, cannot access the static method via the instance")
# access the static member through an instance...
print(b1.num)
print(b2.num)
b3 = Book(12)
print(b1.num)
print(b2.num)
print(b3.num)
