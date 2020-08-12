days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_names = ['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December']
name_to_days_num = {}
for i in range(12):
    name_to_days_num[months_names[i]] = days_in_months[i]
month_name_to_index = {}
for i in range(12):
    month_name_to_index[months_names[i]] = i


def get_num_of_days_in_month(month_name):
    if month_name in name_to_days_num:
        return name_to_days_num[months_name]
    else:
        print('No such month')


def get_following_month(month_name):
    if month_name in name_to_days_num:
        index = month_name_to_index[month_name]
        return months_names[(index + 1) % 12]
    else:
        print('No such month')


# the definition here is not accurate for intersetellar time...


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0
