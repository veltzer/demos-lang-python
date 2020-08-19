"""
This example shows that scope of variables in a python function
is really local
"""


# noinspection PyShadowingNames
def my_function():
    x = 5
    print(x)


x = 7
my_function()
print(x)
