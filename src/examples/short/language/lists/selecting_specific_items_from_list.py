"""
This is an example of how to select specific fields from a list
"""

fields = [3, 4]

data = [1, 2, 3, 4, 5, 6, 7]

selection = [data[x] for x in fields]

print(selection)
