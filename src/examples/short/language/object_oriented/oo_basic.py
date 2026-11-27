#!/usr/bin/env python

"""
A classic oo example
"""

class Book:
    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year
    def print_myself(self) -> None:
        print(f"name is {self.name}")
        print(f"author is {self.author}")
        print(f"year is {self.year}")
    def set_name(self, newname: str) -> None:
        self.name = newname

b=Book("Lord of the Rings", "J.R.R. Tolkien", 1956)
print(dir(b))
