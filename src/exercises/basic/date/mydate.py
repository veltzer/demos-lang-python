"""
Module to handle dates
"""

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_name = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
name_to_days_num = {}
for i in range(12):
    name_to_days_num[months_name[i]] = days_in_months[i]
    # print("setting ",months_name[i],"to",days_in_months[i])


def get_num_of_days_in_month(month_name):
    """ Given a month name,
    return the number of days in this month"""
    if month_name in name_to_days_num:
        return name_to_days_num[month_name]
    raise ValueError("no such month")


def get_following_month(month_name):
    """ Given a month name,
    return the name of the following month"""
    if month_name in name_to_days_num:
        month_number = months_name.index(month_name)
        return months_name[(month_number + 1) % 12]
    raise ValueError("No such month")


def is_leap_year(year):
    """ Return True if the year is a leap year, False otherwise"""
    return year % 4 == 0 and year % 1000 != 0
