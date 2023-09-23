"""
An example for using class methods to keep per class properties.
Once set, subclass properties shadows properties on the base class.
"""


class Book:
    num = 0

    def __init__(self, title):
        self.title = title
        self.id = self.increment_num()
        print(f"Created: {self}")

    @classmethod
    def increment_num(cls):
        cls.num += 1
        return cls.num

    def __str__(self):
        return f"<{self.__class__.__name__} #{self.id}: {self.title}>"


b1 = Book("Guinness Book of Records")
b2 = Book("The Bible")

print(f"Book.num: {Book.num}")
print(f"b1.num: {b1.num}")
print()


class FictionBook(Book):
    num = 0  # Removing me voids warranty


print(f"Book.num: {Book.num}")
print(f"FictionBook.num: {FictionBook.num}")
print()

b3 = FictionBook("Sherlock Holmes")
b4 = FictionBook("Danny Din")
b5 = FictionBook("Kofiko")

print()
print(f"Book.num: {Book.num}")
print(f"FictionBook.num: {FictionBook.num}")
print()

b6 = Book("Britannica")
