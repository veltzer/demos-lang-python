"""
date2
"""

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_names = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
name_to_days_num = {
    months_names[i]: days_in_months[i] for i in range(12)
}


def get_num_of_days_in_month(month_name, year):
    """ Given a month name,
    return the number of days in this month"""
    if month_name in name_to_days_num:
        if month_name == "February" and is_leap_year(year):
            return 29
        return name_to_days_num[month_name]
    raise ValueError("No such month")


def get_following_month(month_name):
    """ Given a month name,
    return the name of the following month"""
    if month_name in name_to_days_num:
        i = months_names.index(month_name)
        return months_names[(i + 1) % 12]
    raise ValueError("No such month")


def is_leap_year(year):
    """ Return True if the year is a leap year, False otherwise"""
    return year % 4 == 0 and (year % 100 != 0 or year % 1000 == 0)
