"""
This is a cheating example since it used the str.count() method.
"""

s = input("Please enter a line of digits: ")
for i in range(10):
    print(f"{i} appeared {s.count(str(i))} times in the text")
