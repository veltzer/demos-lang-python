"""
Example of sorting with python using the key parameter
"""


def compare(item):
    return item[1]


m = {"mark": 10, "yossi": 3, "doron": 67}
arr = list(m.items())
arr.sort(key=compare)

print(arr)
