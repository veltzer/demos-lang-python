"""
This shows some basic formatting.
"""

# pylint: disable=consider-using-f-string

name = "mark"

# by position
print("my name is {}".format(name))
# by number
print("my name is {0}".format(name))
# by name
print("my name is {name}".format(name=name))
# fstring
print(f"my name is {name}")
