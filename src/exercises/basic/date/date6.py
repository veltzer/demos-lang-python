class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __add__(self, days=0, months=0, years=0):
        if isinstance(years, int):
            self.year += years
        if isinstance(months, int):
            self.month += months
        if isinstance(days, int):
            self.day += days
