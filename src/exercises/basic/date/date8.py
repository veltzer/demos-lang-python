from typing import ClassVar, Self

"""
date8
"""


class Date:
    days_in_months: ClassVar = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int, month: int, year: int) -> None:
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            print("Date must be initialized with numbers")
            return
        if month < 1 or month > 12:
            print("Month must be between 1 and 12")
            return
        if day < 0 or day > self.days_in_months[month - 1]:
            print("Day must be between 1 and ", self.days_in_months[month - 1])
            return
        self.day = day  # pyrefly: ignore[possibly-uninitialized-attribute]  teaching: before exceptions, a bad date prints and returns
        self.month = month  # pyrefly: ignore[possibly-uninitialized-attribute]  teaching: before exceptions, a bad date prints and returns
        self.year = year  # pyrefly: ignore[possibly-uninitialized-attribute]  teaching: before exceptions, a bad date prints and returns

    def __gt__(self, other: Self) -> bool:
        """ Overloading operator>for dates """
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month and self.day > other.day:
                return True
        return False

    def __lt__(self, other: Self):
        """ Overloading operator<for dates """
        return other > self

    def __eq__(self, other: object):
        """ Overloading operator==for dates """
        if not isinstance(other, Date):
            return NotImplemented
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __hash__(self) -> int:
        return hash((self.year, self.month, self.day))

    def __ne__(self, other: object) -> bool:
        """ Overloading operator!=for dates """
        return not self == other

    def __le__(self, other: Self):
        """ Overloading operator<=for dates """
        return self < other or self == other

    def __ge__(self, other: Self):
        """ Overloading operator>=for dates """
        return self > other or self == other

    def __str__(self) -> str:
        return str(self.day) + "." + str(self.month) + "." + str(self.year)
