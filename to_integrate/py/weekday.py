# Python 3 version

# Code for reading in the date */
date = input('Please enter date (DD/MM/YYYY): ')
d, m, y = date.split('/')
d = int(d)
m = int(m)
y = int(y)


"""
  Add Your Code Here: to adjust the values of
  d, m and y under certain circumstances

             d contains the day
             m contains the month
             y contains the year
"""

z = 1 + d + (m*2) + (3 * (m+1)//5) + y + y//4 - y//100 + y//400
z %= 7

days = ['Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur']
print(days[z] + 'day')


