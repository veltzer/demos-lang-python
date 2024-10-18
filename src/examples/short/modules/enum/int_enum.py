"""
IntEnum is particularly useful when you need enumerated constants that are also integers,
allowing you to perform integer operations while maintaining the readability and type safety of enums.
"""
from enum import IntEnum


class DaysOfWeek(IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


# Using the IntEnum
print(DaysOfWeek.WEDNESDAY)  # Output: DaysOfWeek.WEDNESDAY
print(DaysOfWeek.WEDNESDAY.value)  # Output: 3

# Comparison
print(DaysOfWeek.FRIDAY > DaysOfWeek.MONDAY)  # Output: True

# Arithmetic operations
print(DaysOfWeek.TUESDAY + 2)  # Output: 4
print(DaysOfWeek(4))  # Output: DaysOfWeek.THURSDAY

# Iteration
for day in DaysOfWeek:
    print(day.name, day.value)

# Conversion to and from integers
day_num = 3
day = DaysOfWeek(day_num)
print(f"Day {day_num} is {day.name}")  # Output: Day 3 is WEDNESDAY
