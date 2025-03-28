"""
Solution
"""


def find_my_value(value):
    for k, v in globals().items():
        if v == value:
            return k
    raise ValueError("could not find value")


x = 5
y = 8
z = [1,2,3]
pi = 3.14

print(find_my_value(3.14))
