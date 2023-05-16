"""
This example shows how to compare dictionaries

Note that in earlier version of python there was a "cmp"
function that compared dictionaries which is now gone.
use the "==" operator instead.

References:
- http://stackoverflow.com/questions/4527942/comparing-two-dictionaries-in-python
"""

dict1 = {"Name": "Mark", "Age": 7}
dict2 = {"Name": "Bernard", "Age": 27}
dict3 = {"Name": "Alfred", "Age": 27}
dict4 = {"Name": "Mark", "Age": 7}
print(dict1 == dict2)
print(dict2 == dict3)
print(dict1 == dict4)
