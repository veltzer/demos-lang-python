#! /usr/local/bin/python

"""
Use a loop to ensure that an integer entered by the user at the keyboard is positive.
Use a second loop to count down from this integer in steps of 2, 
displaying each number on the screen until either 1 or 0 is reached, 
i.e. if the integer 16 (validated) is entered, the output would be:
16 14 12 10 8 6 4 2 0 (on different lines)
and if 7 is entered, the output would be: 
7 5 3 1 (on different lines)
"""

var = input("Please enter an integer: ")

if not var.isdecimal():
    print("Invalid integer:", var)
    exit(1)
    
for var in range(int(var), -1, -2):
    print(var)
