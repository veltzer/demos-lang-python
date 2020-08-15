import mydate

'''
A calendar of events, has an entry for every event,
which is a mapping from event name to Date object
'''


class Calendar:
    def __init__(self):
        self.events = {}

    def add_event(self, name, date):
        """ Add a new entry to the calendar"""
        self.events[name] = date

    def is_event(self, date):
        """ Check if the given date appears in the calendar"""
        return date in self.events.values()

    def get_date(self, name):
        """ Return the date of the given event name"""
        return self.events[name]

    def get_all_events_in_month(self, month):
        """ Return a dictionary with all the events in the given month
        month is the number of the month """
        month_events = {}
        for name in self.events.keys():
            if self.events[name].month == month:
                month_events[name] = self.events[name]
        return month_events


class Date:
    def __init__(self, day, month, year):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            print('Date must be initialized with numbers')
            return
        if month < 1 or month > 12:
            print('Month must be between 1 and 12')
            return
        if mydate.is_leap_year(year):
            days = mydate.days_in_months_leap_year[month - 1]
        else:
            days = mydate.days_in_months[month - 1]
        if day < 1 or day > days:
            print('Day must be between 1 and ', days)
            return
        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, other):
        """ Overloading operator>for dates """
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
        return False

    def __lt__(self, other):
        """ Overloading operator<for dates """
        return other > self

    def __eq__(self, other):
        """ Overloading operator==for dates """
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        """ Overloading operator!=for dates """
        return not (self == other)

    def __le__(self, other):
        """ Overloading operator<=for dates """
        return self < other or self == other

    def __ge__(self, other):
        """ Overloading operator>=for dates """
        return self > other or self == other

    def __str__(self):
        return str(self.day) + '.' + str(self.month) + '.' + str(self.year)
