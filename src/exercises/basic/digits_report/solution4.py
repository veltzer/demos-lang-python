"""
This is a cheating example since it used the str.count() method.
"""

s = input('Please enter a line of digits: ')
for i in range(10):
    print('{i} appeared {count} times in the text'.format(
        i=i, count=s.count(str(i))))
