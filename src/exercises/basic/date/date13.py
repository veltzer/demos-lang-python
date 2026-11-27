"""
date13
"""

from typing import Any, Self

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_names = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
name_to_days_num = {
    months_names[i]: days_in_months[i] for i in range(12)
}


def get_num_of_days_in_month(month_name: str) -> int:
    """ Given a month name,
    return the number of days in this month"""
    if month_name in name_to_days_num:
        return name_to_days_num[month_name]
    raise ValueError("No such month")


def get_following_month(month_name: str) -> str:
    """ Given a month name,
    return the name of the following month"""
    if month_name in name_to_days_num:
        i = months_names.index(month_name)
        return months_names[(i + 1) % 12]
    raise ValueError("No such month")


def is_leap_year(year: int):
    """ Return True if the year is a leap year, False otherwise"""
    return year % 4 == 0 and (year % 100 != 0 or year % 1000 == 0)


class Calendar:
    """ A calendar of events, has an entry for every event,
            which is a mapping from event name to Date object"""

    def __init__(self) -> None:
        self.events = {}

    def add_event(self, name: str, date: Any) -> None:
        """ Add a new entry to the calendar"""
        self.events[name] = date

    def is_event(self, date: Any) -> bool:
        """ Check if the given date appears in the calendar"""
        return date in self.events.values()

    def get_date(self, name: str):
        """ Return the date of the given event name"""
        return self.events[name]

    def get_all_events_in_month(self, month: int):
        """ Return a dictionary with all the events in the given month
        month is the number of the month """
        return {name: e for name, e in self.events.items() if e.month == month}


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            print("Date must be initialized with numbers")
            return
        if month < 1 or month > 12:
            print("Month must be between 1 and 12")
            return
        if is_leap_year(year) and month == 2:
            if day < 0 or day > 29:
                print("Day must be between 1 and ", days_in_months[month - 1])
                return
        elif day < 0 or day > days_in_months[month - 1]:
            print("Day must be between 1 and ", days_in_months[month - 1])
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
        """ Overloading operator >= for dates """
        return self > other or self == other

    def __str__(self) -> str:
        return str(self.day) + "." + str(self.month) + "." + str(self.year)
