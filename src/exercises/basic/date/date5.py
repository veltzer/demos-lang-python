days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_names = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
name_to_days_num = {
    months_names[i]: days_in_months[i] for i in range(12)
}


def get_num_of_days_in_month(month_name):
    """ Given a month name,
    return the number of days in this month"""
    if month_name in name_to_days_num:
        return name_to_days_num[months_names]
    raise DateException('No such month name')


def get_following_month(month_name):
    """ Given a month name,
    return the name of the following month"""
    if month_name in name_to_days_num:
        i = months_names.index(month_name)
        return months_names[(i + 1) % 12]
    raise DateException('No such month name')


def is_leap_year(year):
    """ Return True if the year is a leap year, False otherwise"""
    return year % 4 == 0 and year % 1000 != 0


class Calendar:
    """ A calendar of events, has an entry for every event,
    which is a mapping from event name to Date object"""

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
        for name, e in self.events.items():
            if e.month == month:
                month_events[name] = e
        return month_events


class Date:
    def __init__(self, day, month, year):
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise DateException('Date must be initialized with numbers')
        if month < 1 or month > 12:
            raise DateException('Month must be between 1 and 12')
        if is_leap_year(year):
            if day < 0 or day > days_in_months_leap_year[month - 1]:
                raise DateException(f"Day must be between 1 and {days_in_months[month - 1]}")
            if day < 0 or day > days_in_months[month - 1]:
                raise DateException(f"Day must be between 1 and {days_in_months[month - 1]}")

        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, other):
        """ Overloading operator>for dates """
        if self.year > other.year:
            return True
        if self.year == other.year:
            if self.month > other.month:
                return True
            if self.month == other.month:
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
        return not self == other

    def __le__(self, other):
        """ Overloading operator<=for dates """
        return self < other or self == other

    def __ge__(self, other):
        """ Overloading operator>=for dates """
        return self > other or self == other

    def __str__(self):
        return str(self.day) + '.' + str(self.month) + '.' + str(self.year)


class DateException(Exception):
    pass
