#!/usr/bin/env python

class Book:
    def __init__(self, name, author, year) -> None:
        self.name = name
        self.author = author
        self.year = year
        self.__publisher = "Simon and Shuschter"
    def print_myself(self):
        print(f"name is {self.name}")
        print(f"author is {self.author}")
        print(f"year is {self.year}")
    def set_name(self, newname):
        self.name = newname

b=Book("Lord of the Rings", "J.R.R. Tolkien", 1956)
print(dir(b))
