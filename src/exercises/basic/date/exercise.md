# Date

Write a module for dealing with dates.
It will have a mapping from month name to number of days in that month, and also from month number to month name.

The following functions should be defined:

```python
get_num_of_days_in_month(month_name)
get_following_month(month_name)
is_leap_year(year)
```

hint:
What is a leap year?
A year is a leap year if it is divisible by 4 not divisible by 100 unless divisible by 400.

Edit your date module:
Write a class that represents a Date.
It will be initialized from 3 numbers: day, month, year. The __init__ method will check the validity of the arguments.
Overload the operators: >, < , ==, !=, <=, >=.
Write an __str__() method.

The data defined previously in the module will be used for validity checking of the dates.

Write a class Calendar.
It will have the attribute events – a mapping from event name to date object.
Write the following methods:

```python
Get_date(self, name)
add_event(self, name, date)
is_event(self,date)
get_all_events_in_month(self,month)

Write a script which creates a calendar from a file built as described below :
Event_name day.month.year
Event_name day.month.year
Event_name day.month.year
```

Hint: The module time can tell you what the current month is.

## Add exceptions

* Go over the classes you wrote in the previous exercise.
* Add exception handling everywhere it is needed. (Raise an exception for invalid arguments).
* You might want to write your own exceptions for that.
* The calendar creating script will handle the exceptions.
