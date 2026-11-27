"""
date6
"""


class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __add__(self, days: int = 0, months: int = 0, years: int = 0) -> None:
        if isinstance(years, int):
            self.year += years
        if isinstance(months, int):
            self.month += months
        if isinstance(days, int):
            self.day += days
